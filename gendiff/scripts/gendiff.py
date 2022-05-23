"""Script for run gendiff."""
#!/usr/bin/env python3 # noqa:E265


from gendiff.diff import generate_diff
from gendiff.parser import parse_cli_args
from gendiff.decode_files import decode_files
import gendiff.stylish


def main():
    formatter = gendiff.stylish.format_diff_to_string
    print(formatter(generate_diff(*decode_files(*parse_cli_args()))), end="")


if __name__ == "__main__":
    main()
