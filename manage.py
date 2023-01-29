#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from scrapdata import GetCash


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskyukon.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def update_database():
    obj = GetCash()
    two_lists = obj.get_data()
    dict_conv = obj.convert_data_to_dict(two_lists)
    obj.update_data(dict_conv)


if __name__ == '__main__':
    # print("Updating database!")
    # update_database()
    # print("Database has chenged")
    main()
