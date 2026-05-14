#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')  # Uncomment untuk production
>>>>>>> cd3e56c59ccf7ab44a93fcfe70c2af3823da149d
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
