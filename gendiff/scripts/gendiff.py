"""Script for run gendiff."""
#!/usr/bin/env python3 # noqa:E265


from gendiff.diff import generate_diff
from gendiff.cli import parse_args


def main():
    """Main entry point of the 'gendiff' app."""
    first_file, second_file, format_name = parse_args()
    print(generate_diff(first_file, second_file, format_name))


if __name__ == "__main__":
    main()
