"""Parse CLI arguments."""


import argparse


def parse_cli_args():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    return first_file, second_file
