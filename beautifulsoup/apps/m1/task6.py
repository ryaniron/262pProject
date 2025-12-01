# task6.py - Change all <b> tags to <blockquote> tags and write the tree onto a file
# Usage: python task6.py input.html
from common import build_arg_parser, load_soup, write_text, default_out_path, maybe_timed

@maybe_timed(True)
def do_work(args):
    soup = load_soup(args.input, parser=args.parser, encoding=args.encoding)
    count = 0
    for b in soup.find_all("b"):
        b.name = "blockquote"
        count += 1
    out_path = args.output or default_out_path(args.input, ".b_to_blockquote.html")
    write_text(out_path, soup.prettify())
    print(f"Rewrote {count} <b> tags to <blockquote>. Wrote: {out_path}")

if __name__ == "__main__":
    parser = build_arg_parser("Task 6: Convert <b> -> <blockquote> and write output")
    args = parser.parse_args()
    do_work(args)
