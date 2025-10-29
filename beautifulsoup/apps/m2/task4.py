# task4_soupstrainer.py – Print all tags that have an id attribute using SoupStrainer
# Usage: python task4_soupstrainer.py input.html
#
# Optimization rationale:
# -----------------------
# The lambda filter ensures that only tags containing an "id" attribute
# are parsed into the tree at all, greatly reducing memory footprint
# on large documents.

from bs4 import BeautifulSoup, SoupStrainer
from common import build_arg_parser, maybe_timed

@maybe_timed(True)
def do_work(args):
    # Filter parses only elements that have an 'id' attribute
    strainer = SoupStrainer(lambda tag: tag.has_attr("id"))

    with open(args.input, "r", encoding=args.encoding or "utf-8") as f:
        soup = BeautifulSoup(f, args.parser, parse_only=strainer)

    with_ids = soup.find_all(True, id=True)
    for i, el in enumerate(with_ids, 1):
        print(f"{i:03d}. <{el.name} id={el.get('id')!r}>")

    if not with_ids:
        print("No elements with an 'id' attribute found.")

if __name__ == "__main__":
    parser = build_arg_parser("Task 4 (SoupStrainer): Print all tags with an id attribute")
    args = parser.parse_args()
    do_work(args)
