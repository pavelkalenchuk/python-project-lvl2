"""Script for run gendiff."""
#!/usr/bin/env python3 # noqa:E265


import argparse


parser = argparse.ArgumentParser(description="Generate diff")
parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format of output")


parser.parse_args()


""" parser = argparse.ArgumentParser(
    description="Generate diff"
)
parser.add_argument(
    'integers',
    metavar='first_file',
    type=str, nargs='+',
    help=''
)

parser.add_argument(
    'integers',
    metavar='second_file',
    type=str, nargs='+',
    help=''
) """
