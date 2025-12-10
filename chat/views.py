from __future__ import annotations

import logging
import os
import json
from typing import List

import requests
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from requests import RequestException

from .prompts import SYSTEM_PROMPT

logger = logging.getLogger(__name__)

LLM_ENDPOINT = os.environ.get('FLASHCARD_LLM_ENDPOINT', 'http://127.0.0.1:8011/v1/chat/completions')
LLM_MODEL = os.environ.get('FLASHCARD_LLM_MODEL', '')
LLM_TIMEOUT = float(os.environ.get('FLASHCARD_LLM_TIMEOUT', '150'))
flash_cards: dict[str, str] = {}

def _fetch_llm_reply(user_message: str, endpoint: str | None = None, model: str | None = None, api_key: str | None = None) -> str | None:
    """Fetch LLM reply for a single user message (no conversation history)."""
    llm_endpoint = endpoint or LLM_ENDPOINT
    llm_model = model or LLM_MODEL
    messages = [
        {'role': 'user', 'content': SYSTEM_PROMPT + user_message}
    ]
    payload = {
        'model': llm_model,
        'messages': messages,
    }
    headers = {}
    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'
    try:
        response = requests.post(
            llm_endpoint,
            json=payload,
            headers=headers,
            timeout=LLM_TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()
        choices = data.get('choices') or []
        return (choices[0].get('message') or {}).get('content') if choices else None
    except (RequestException, ValueError, KeyError) as exc:
        logger.exception('LLM request failed: %s', exc)
        return None


def _fallback_reply() -> str:
    return (
        "I'm having trouble reaching the AI backend right now. "
        "Please try again in a moment."
    )


@require_http_methods(['GET', 'POST'])
def chat_home(request):
    global flash_cards
    result = None
    user_prompt = None
    llm_endpoint = None
    llm_model = None
    api_key = None
    current_flash_cards = {}
    file_path = None
    
    if request.method == 'POST':
        user_prompt = request.POST.get('message', '').strip()
        llm_endpoint = request.POST.get('llm_endpoint', '').strip() or None
        llm_model = request.POST.get('llm_model', '').strip() or None
        api_key = request.POST.get('api_key', '').strip() or None
        if user_prompt:
            raw_reply = _fetch_llm_reply(user_prompt, llm_endpoint, llm_model, api_key) or _fallback_reply()
            print('Raw reply: %s', raw_reply)
            current_flash_cards = {}
            if raw_reply:
                # Remove markdown code block markers
                cleaned_reply = raw_reply.strip()
                if cleaned_reply.startswith('```json'):
                    cleaned_reply = cleaned_reply[7:].strip()
                elif cleaned_reply.startswith('```'):
                    cleaned_reply = cleaned_reply[3:].strip()
                if cleaned_reply.endswith('```'):
                    cleaned_reply = cleaned_reply[:-3].strip()
                
                try:
                    current_flash_cards = json.loads(cleaned_reply)
                    flash_cards = current_flash_cards
                    # Save flash cards to file
                    if current_flash_cards:
                        keys_line = ';'.join(f'"{key.replace('"', '""')}"' for key in current_flash_cards.keys())
                        values_line = ';'.join(f'"{value.replace('"', '""')}"' for value in current_flash_cards.values())
                        file_path = os.path.abspath('flash_cards.txt')
                        with open('flash_cards.txt', 'w', encoding='utf-8') as f:
                            f.write(keys_line + '\n')
                            f.write(values_line + '\n')
                except json.JSONDecodeError:
                    logger.exception('Failed to parse LLM response as JSON')
            first_question = next(iter(current_flash_cards.keys()), None)
            result = first_question or raw_reply

    return render(
        request,
        'chat/index.html',
        {
            'result': result,
            'user_prompt': user_prompt,
            'llm_endpoint': llm_endpoint or LLM_ENDPOINT,
            'llm_model': llm_model or LLM_MODEL,
            'api_key': api_key or '',
            'flash_cards': current_flash_cards,
            'flash_cards_json': json.dumps(current_flash_cards),
            'file_path': file_path,
        },
    )
