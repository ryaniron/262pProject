# task1.py - Pretty-print (prettify) an HTML/XML file
# Usage: python task1.py input.html
from common import build_arg_parser, load_soup, write_text, default_out_path, maybe_timed

@maybe_timed(True)
def do_work(args):
    soup = load_soup(args.input, parser=args.parser, encoding=args.encoding)
    out_path = args.output or default_out_path(args.input, ".pretty.html")
    write_text(out_path, soup.prettify())
    print(f"Wrote prettified tree to: {out_path}")

if __name__ == "__main__":
    parser = build_arg_parser("Task 1: Read file -> prettify -> write to disk")
    args = parser.parse_args()
    do_work(args)
