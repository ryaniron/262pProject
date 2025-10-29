from bs4 import BeautifulSoup
from bs4.soup_replacer import SoupReplacer

html = "<b>Hello</b><b>World</b>"
soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("b", "blockquote"))
print(soup.prettify())