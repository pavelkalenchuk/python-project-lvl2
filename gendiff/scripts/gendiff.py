"""Script for run gendiff."""
#!/usr/bin/env python3 # noqa:E265


import argparse
from gendiff.engine import generate_diff


def main():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file

    print(generate_diff(first_file, second_file))


if __name__ == "__main__":
    main()
