class SoupReplacer:
    """
    A simple class that replaces all tags 'og_tag' with 'alt_tag'
    during parsing.
    Example:
        replacer = SoupReplacer("b", "blockquote")
        BeautifulSoup(html, "html.parser", replacer=replacer)
    """
    def __init__(self, og_tag, alt_tag):
        self.og_tag = og_tag
        self.alt_tag = alt_tag
