#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer

def add_class_attr(tag):
    if tag.name == "p":
        tag.attrs["class"] = "test"

def main():
    with open("input.html") as f:
        html = f.read()

    replacer = SoupReplacer(xformer=add_class_attr)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    with open("output_task7.html", "w") as out:
        out.write(soup.prettify())

    print("All <p> tags now have class='test' added during parsing.")

if __name__ == "__main__":
    main()
