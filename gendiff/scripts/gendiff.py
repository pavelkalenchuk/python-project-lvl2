"""Script for run gendiff."""
#!/usr/bin/env python3 # noqa:E265


from gendiff.diff import generate_diff
from gendiff.parser import parse_cli_args
from gendiff.decode_files import decode_files
from gendiff.stylish import format_diff_to_string


def main():
    # first_file, second_file = parse_cli_args()
    # print(generate_diff(*decode_files(*parse_cli_args())))
    print(format_diff_to_string(generate_diff(*decode_files(*parse_cli_args()))))


if __name__ == "__main__":
    main()
