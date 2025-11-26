import pytest
from bs4 import BeautifulSoup

def test_iter_simple_document():
    soup = BeautifulSoup("<p>Hello</p>", "html.parser")
    nodes = list(iter(soup))
    assert any(n.name == "p" for n in nodes)

def test_iter_includes_strings():
    soup = BeautifulSoup("<p>Hello</p>", "html.parser")
    nodes = list(soup)
    assert any(str(n) == "Hello" for n in nodes)

def test_iter_nested_structure():
    soup = BeautifulSoup("<div><p>A</p><p>B</p></div>", "html.parser")
    names = [getattr(n, "name", None) for n in soup]
    assert names.count("p") == 2

def test_iter_order_is_depth_first():
    soup = BeautifulSoup("<div><p>A</p><span>B</span></div>", "html.parser")
    result = [str(n) for n in soup]
    # depth-first order must find <p> before <span>
    assert result.index("A") < result.index("B")

def test_iter_comments_and_doctype():
    soup = BeautifulSoup("<!DOCTYPE html><!--hi--><p>x</p>", "html.parser")
    found_comment = any(n.string == "hi" for n in soup if hasattr(n, "string"))
    assert found_comment
