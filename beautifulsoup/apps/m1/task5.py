# task5.py - Use find_parent() meaningfully
# Select a target via CSS (e.g., 'a.some-class') and optionally restrict the parent tag name.
#
# Usage:
#   python task5.py input.html --select "a" --parent "nav"
# If --select is omitted, defaults to the first <a>; if --parent omitted, prints the immediate parent.
from common import build_arg_parser, load_soup, maybe_timed
import argparse

def parser_with_extras():
    p = build_arg_parser("Task 5: Demonstrate find_parent()")
    p.add_argument("--select", default=None, help="CSS selector to pick a node (default: first <a>)")
    p.add_argument("--parent", default=None, help="Restrict parent to this tag name (e.g., 'div', 'nav')")
    p.add_argument("--limit", type=int, default=1, help="How many matches from --select to show (default: 1)")
    return p

@maybe_timed(True)
def do_work(args):
    soup = load_soup(args.input, parser=args.parser, encoding=args.encoding)
    targets = soup.select(args.select) if args.select else soup.find_all("a")
    if not targets:
        print("No target elements found.")
        return
    for idx, t in enumerate(targets[:args.limit], 1):
        print(f"Target {idx}: <{t.name}> text={t.get_text(strip=True)!r}")
        if args.parent:
            par = t.find_parent(args.parent)
            if par:
                print(f"  -> nearest <{args.parent}> parent: <{par.name} class={par.get('class')} id={par.get('id')}>")
            else:
                print(f"  -> no <{args.parent}> parent found")
        else:
            par = t.find_parent()
            if par:
                print(f"  -> immediate parent: <{par.name} class={par.get('class')} id={par.get('id')}>")
            else:
                print("  -> no parent found")

if __name__ == "__main__":
    args = parser_with_extras().parse_args()
    do_work(args)
