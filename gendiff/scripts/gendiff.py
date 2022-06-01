"""Script for run gendiff."""
#!/usr/bin/env python3 # noqa:E265


from gendiff.diff import generate_diff
from gendiff.parser import parse_cli_args
from gendiff.decode_files import decode_files
from gendiff.formaters.stylish import format_diff_to_string
from gendiff.formaters.plain import format_diff_to_plain
from gendiff.formaters.jsonish import format_diff_to_json

format = {
    "stylish": format_diff_to_string,
    "plain": format_diff_to_plain,
    "json": format_diff_to_json,
}


def main():
    first_file, second_file, formatter = parse_cli_args()
    print(format[formatter](generate_diff(*decode_files(first_file, second_file))))


if __name__ == "__main__":
    main()
