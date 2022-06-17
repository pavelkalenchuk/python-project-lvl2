"""Parse CLI arguments."""


import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format", default="stylish", help="set format of output"
    )

    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    formatter = args.format
    return first_file, second_file, formatter
