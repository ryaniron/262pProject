from bs4 import BeautifulSoup, SoupStrainer
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="HTML file to process")
    parser.add_argument("--parser", default="lxml", help="Parser to use")
    args = parser.parse_args()

    # Read the input HTML
    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()

    # SoupStrainer: only parse tags that have an id attribute
    def has_id(tag_name, attrs):
        return attrs is not None and "id" in attrs

    strainer = SoupStrainer(name=has_id)

    # Parse ONLY relevant nodes
    soup = BeautifulSoup(content, args.parser, parse_only=strainer)

    # Print all tags that were kept
    for tag in soup.find_all(True):
        print(tag)
        print("----")

if __name__ == "__main__":
    main()
