#!/usr/bin/env python3
from bs4 import BeautifulSoup
import sys

def main():
    with open(sys.argv[1]) as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    for node in soup:
        print(repr(node))

if __name__ == "__main__":
    main()
