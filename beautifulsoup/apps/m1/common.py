# common.py
import argparse
import sys
import time
from bs4 import BeautifulSoup

def build_arg_parser(description):
    p = argparse.ArgumentParser(description=description)
    p.add_argument("input", help="Path to the HTML/XML file to process")
    p.add_argument("-p", "--parser", default="lxml", choices=["lxml", "html.parser", "xml"],
                   help="Parser to use (default: lxml). Use 'xml' for XML files.")
    p.add_argument("-o", "--output", help="Optional path for output file")
    p.add_argument("--encoding", default=None, help="File encoding if not UTF-8/auto-detected")
    p.add_argument("--time", action="store_true", help="Measure elapsed time")
    return p

def open_text(path, encoding=None):
    # Graceful open with provided encoding or default.
    if encoding:
        return open(path, "r", encoding=encoding, errors="replace")
    # Try utf-8 then fall back to latin-1 for robustness
    try:
        return open(path, "r", encoding="utf-8")
    except UnicodeDecodeError:
        return open(path, "r", encoding="latin-1", errors="replace")

def load_soup(path, parser="lxml", encoding=None):
    with open_text(path, encoding) as f:
        data = f.read()
    if parser == "xml":
        bs_parser = "xml"
    else:
        bs_parser = parser
    return BeautifulSoup(data, bs_parser)

def write_text(path, text, encoding="utf-8"):
    with open(path, "w", encoding=encoding) as f:
        f.write(text)

def default_out_path(in_path, suffix):
    from pathlib import Path
    p = Path(in_path)
    return str(p.with_suffix(p.suffix + suffix))

def maybe_timed(enabled):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            if not enabled:
                return fn(*args, **kwargs)
            start = time.perf_counter()
            result = fn(*args, **kwargs)
            end = time.perf_counter()
            print(f"[elapsed] {end - start:.3f} s", file=sys.stderr)
            return result
        return wrapper
    return decorator
