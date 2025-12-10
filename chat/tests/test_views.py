import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_chat_home_bootstraps_conversation(client):
    url = reverse('chat:home')

    response = client.get(url)

    assert response.status_code == 200
    session = client.session
    assert 'conversation' in session
    assert session['conversation'][0]['role'] == 'assistant'
    assert 'demo' in session['conversation'][0]['content'].lower()


@pytest.mark.django_db
def test_chat_home_records_user_prompt_and_bot_reply(client, monkeypatch):
    monkeypatch.setattr('chat.views._fetch_llm_reply', lambda conversation: 'LLM says hi')

    url = reverse('chat:home')
    client.get(url)  # primes the conversation

    response = client.post(url, {'message': 'Hello there'})

    assert response.status_code == 302
    session = client.session
    conversation = session['conversation']
    assert conversation[-2]['role'] == 'user'
    assert conversation[-2]['content'] == 'Hello there'
    assert conversation[-1]['role'] == 'assistant'
    assert conversation[-1]['content'] == 'LLM says hi'


@pytest.mark.django_db
def test_chat_home_fallback_when_llm_unavailable(client, monkeypatch):
    monkeypatch.setattr('chat.views._fetch_llm_reply', lambda conversation: None)

    url = reverse('chat:home')
    client.get(url)

    response = client.post(url, {'message': 'test'})

    assert response.status_code == 302
    conversation = client.session['conversation']
    assert 'trouble reaching the ai backend' in conversation[-1]['content'].lower()

