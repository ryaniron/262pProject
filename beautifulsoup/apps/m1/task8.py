# task8.py
#  Remove <script> and <style> tags (decompose)
#  Unwrap all <span> tags (keep content, drop wrapper)
#  Print first 200 chars of visible text
#  Write cleaned file
# Usage: python task8.py input.html [-o OUTPUT] [--parser ...] [--time]
from common import build_arg_parser, load_soup, write_text, default_out_path, maybe_timed

@maybe_timed(True)
def do_work(args):
    soup = load_soup(args.input, parser=args.parser, encoding=args.encoding)
    # remove scripts/styles
    removed = 0
    for t in soup(["script", "style"]):
        t.decompose()
        removed += 1
    # unwrap span tags
    unwrapped = 0
    for sp in soup.find_all("span"):
        sp.unwrap()
        unwrapped += 1
    # print a text preview
    text = soup.get_text(" ", strip=True)
    preview = text[:200]
    print(f"Removed {removed} <script/style> tags; unwrapped {unwrapped} <span> tags.")
    print("Text preview (first 200 chars):")
    print(preview)
    # write cleaned
    out_path = args.output or default_out_path(args.input, ".cleaned.html")
    write_text(out_path, soup.prettify())
    print(f"Wrote cleaned file: {out_path}")

if __name__ == "__main__":
    parser = build_arg_parser("Task 8: Extra API usage (decompose, unwrap, text)")
    args = parser.parse_args()
    do_work(args)
