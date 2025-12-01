# task2.py - Print all hyperlinks (<a> tags)
# Usage: python task2.py input.html 
from common import build_arg_parser, load_soup, maybe_timed
import sys

@maybe_timed(True)
def do_work(args):
    soup = load_soup(args.input, parser=args.parser, encoding=args.encoding)
    links = soup.find_all("a")
    for i, a in enumerate(links, 1):
        href = a.get("href", "")
        text = (a.get_text(strip=True) or "").replace("\n", " ")
        print(f"{i:03d}. href={href!r}  text={text!r}")
    if not links:
        print("No <a> tags found.", file=sys.stderr)

if __name__ == "__main__":
    parser = build_arg_parser("Task 2: Print all <a> hyperlinks")
    args = parser.parse_args()
    do_work(args)
