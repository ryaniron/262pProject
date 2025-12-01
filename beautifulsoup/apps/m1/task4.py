# task4.py - Print all tags that have an id attribute (single API call via CSS selector)
# Usage: python task4.py input.html
from common import build_arg_parser, load_soup, maybe_timed

@maybe_timed(True)
def do_work(args):
    soup = load_soup(args.input, parser=args.parser, encoding=args.encoding)
    # Single API call: CSS selector '[id]' returns all elements with an id attribute.
    with_ids = soup.select("[id]")
    for i, el in enumerate(with_ids, 1):
        print(f"{i:03d}. <{el.name} id={el.get('id')!r}>")
    if not with_ids:
        print("No elements with an 'id' attribute found.")

if __name__ == "__main__":
    parser = build_arg_parser("Task 4: Print all tags that have an id attribute")
    args = parser.parse_args()
    do_work(args)
