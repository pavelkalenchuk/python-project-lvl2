"""Script for run gendiff."""
#!/usr/bin/env python3 # noqa:E265


from gendiff.diff import generate_diff
from gendiff.parser import parse_cli_args


def main():
    first_file, second_file, format_name = parse_cli_args()
    print(generate_diff(first_file, second_file, format_name))


if __name__ == "__main__":
    main()
