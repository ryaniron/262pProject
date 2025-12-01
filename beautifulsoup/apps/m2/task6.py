# # task6_replacer.py - Replaces all <b> tags with <blockquote> during parsing using SoupReplacer
# # Usage: python task6.py input.html

# apps/m2/task6.py
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer
from common import build_arg_parser, maybe_timed


@maybe_timed(True)
def do_work(args):
    # Read file
    with open(args.input, "r", encoding=args.encoding or "utf-8") as f:
        html = f.read()

    # Use Milestone-2 SoupReplacer (simple mapping)
    replacer = SoupReplacer("b", "blockquote")

    # Parse HTML with SoupReplacer
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # Write output
    output_file = "task6_output.html"
    with open(output_file, "w", encoding="utf-8") as out:
        out.write(soup.prettify())

    print(f"✔ All <b> tags were replaced with <blockquote> DURING PARSING.")
    print(f"✔ Output written to {output_file}")


if __name__ == "__main__":
    parser = build_arg_parser("Milestone 2 — Task 6 (SoupReplacer: b → blockquote)")
    args = parser.parse_args()
    do_work(args)


# from bs4 import BeautifulSoup
# from bs4.soup_replacer import SoupReplacer
# from common import build_arg_parser, maybe_timed

# @maybe_timed(True)
# def do_work(args):
#     with open(args.input, "r", encoding=args.encoding or "utf-8") as f:
#         html = f.read()

#     replacer = SoupReplacer("b", "blockquote")
#     soup = BeautifulSoup(html, "html.parser", replacer=replacer)

#     with open("output_replaced.html", "w", encoding="utf-8") as out:
#         out.write(soup.prettify())

#     print("All <b> tags replaced with <blockquote> during parsing.")


# if __name__ == "__main__":
#     parser = build_arg_parser("Task 6 (SoupReplacer): Replace <b> with <blockquote>")
#     args = parser.parse_args()
#     do_work(args)
