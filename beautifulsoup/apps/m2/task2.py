# task2_soupstrainer.py – Print all hyperlinks (<a> tags) using SoupStrainer
# Usage: python task2_soupstrainer.py input.html
#
# Optimization rationale:
# -----------------------
# In Milestone-1, BeautifulSoup parsed the entire file before extracting <a> tags.
# Now we restrict parsing to <a> elements only with SoupStrainer, saving time
# and memory when working with large HTML files.

from bs4 import BeautifulSoup, SoupStrainer
from common import build_arg_parser, load_soup, maybe_timed
import sys

@maybe_timed(True)
def do_work(args):
    # SoupStrainer configured to parse only <a> tags
    strainer = SoupStrainer("a")
    with open(args.input, "r", encoding=args.encoding or "utf-8") as f:
        soup = BeautifulSoup(f, args.parser, parse_only=strainer)

    links = soup.find_all("a")
    for i, a in enumerate(links, 1):
        href = a.get("href", "")
        text = (a.get_text(strip=True) or "").replace("\n", " ")
        print(f"{i:03d}. href={href!r}  text={text!r}")

    if not links:
        print("No <a> tags found.", file=sys.stderr)


if __name__ == "__main__":
    parser = build_arg_parser("Task 2 (SoupStrainer): Print all <a> hyperlinks")
    args = parser.parse_args()
    do_work(args)
