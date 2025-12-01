# task3.py - Print all tags in the document (name and count; then a flat listing)
# Usage: python task3.py input.html
from collections import Counter
from common import build_arg_parser, load_soup, maybe_timed

@maybe_timed(True)
def do_work(args):
    soup = load_soup(args.input, parser=args.parser, encoding=args.encoding)
    all_tags = soup.find_all(True)  # True = match any tag
    counts = Counter(tag.name for tag in all_tags)
    print("# Tag counts:")
    for name, cnt in counts.most_common():
        print(f"{name}: {cnt}")
    print("\n# Flat listing of tags in document order:")
    for i, tag in enumerate(all_tags, 1):
        print(f"{i:04d}. <{tag.name}>")

if __name__ == "__main__":
    parser = build_arg_parser("Task 3: Print all tags")
    args = parser.parse_args()
    do_work(args)
