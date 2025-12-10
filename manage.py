#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def _ensure_user_site_available():
    """Guarantee that user-level site-packages are on sys.path.

    On some managed environments PYTHONNOUSERSITE is enabled, which prevents
    Django (installed with --user) from being discovered. We detect the
    expected user site directory and prepend it to sys.path when necessary.
    """
    major, minor = sys.version_info[:2]
    user_site = Path.home() / f'.local/lib/python{major}.{minor}/site-packages'
    if user_site.exists() and str(user_site) not in sys.path:
        sys.path.insert(0, str(user_site))


def main():
    """Run administrative tasks."""
    _ensure_user_site_available()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flashcard.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
