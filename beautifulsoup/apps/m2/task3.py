# task3_soupstrainer.py – Print all tags in the document using SoupStrainer
# Usage: python task3_soupstrainer.py input.html
#
# Optimization rationale:
# -----------------------
# Instead of building the full parse tree, we ask BeautifulSoup (via SoupStrainer)
# to process only tag nodes (ignore comments, strings, and whitespace).
# For very large files, this can dramatically reduce parsing time.

from bs4 import BeautifulSoup, SoupStrainer
from collections import Counter
from common import build_arg_parser, maybe_timed

@maybe_timed(True)
def do_work(args):
    # SoupStrainer(True) means "include all tags", skip non-tag content
    strainer = SoupStrainer(True)
    with open(args.input, "r", encoding=args.encoding or "utf-8") as f:
        soup = BeautifulSoup(f, args.parser, parse_only=strainer)

    all_tags = soup.find_all(True)
    counts = Counter(tag.name for tag in all_tags)

    print("# Tag counts:")
    for name, cnt in counts.most_common():
        print(f"{name}: {cnt}")

    print("\n# Flat listing of tags in document order:")
    for i, tag in enumerate(all_tags, 1):
        print(f"{i:04d}. <{tag.name}>")

if __name__ == "__main__":
    parser = build_arg_parser("Task 3 (SoupStrainer): Print all tags")
    args = parser.parse_args()
    do_work(args)
