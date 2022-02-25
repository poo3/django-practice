#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# cacheを作らないようにする
# https://qiita.com/Kobayashi2019/items/03e31ee50b924f428e71
sys.dont_write_bytecode = True

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TemplateProject.settings')
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
