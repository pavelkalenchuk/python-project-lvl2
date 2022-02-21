"""Package CLI tool."""
from gendiff.engine import generate_diff  # noqa F401
from gendiff.decode_files import decode_files  # noqa F401


__all__ = ("generate_diff", "decode_files")
