"""MOdule for decode jsonm yaml, yml files to python dicttionaries"""

import os
import json
import yaml


def decode_files(first_file, second_file):
    extension = os.path.splitext(first_file)[1]
    file_types = {
        ".json": json.load,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load,
    }
    file1 = file_types[extension](open(first_file))
    file2 = file_types[extension](open(second_file))
    return file1, file2
