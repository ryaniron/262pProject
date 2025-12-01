# task7.py - Add/replace class="test" on all <p> tags and write the tree
from common import build_arg_parser, load_soup, write_text, default_out_path, maybe_timed

@maybe_timed(True)
def do_work(args):
    soup = load_soup(args.input, parser=args.parser, encoding=args.encoding)
    ps = soup.find_all("p")
    for tag in ps:
        tag['class'] = ['test']
    out_path = args.output or default_out_path(args.input, ".p_class_test.html")
    write_text(out_path, soup.prettify())
    print(f"Updated {len(ps)} <p> tags. Wrote: {out_path}")

if __name__ == "__main__":
    parser = build_arg_parser("Task 7: Set class='test' on all <p> tags")
    args = parser.parse_args()
    do_work(args)
