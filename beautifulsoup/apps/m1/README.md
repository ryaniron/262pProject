# BeautifulSoup Tasks (task1.py … task8.py)

## Setup
```bash
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Input corpus
Collect at least 10 HTML/XML files: a mix of small, medium, large, and **one very large (~1 GB)** file. Include at least one with **very nested** structure.
Examples to consider (you choose and download them yourself):
- Small: simple HTML snippets, W3C examples
- Medium: news/article pages, docs pages
- Large: full saved docs (MDN pages, Wikipedia dumps)
- Very large: HTML/XML dumps, large generated HTML for testing

## Parsers
All tasks accept `--parser` with `lxml` (default), `html.parser`, or `xml` for XML content.

## Tasks
1. **task1.py** — Prettify input and write to `*.pretty.html`.
2. **task2.py** — Print all hyperlinks (`<a>`), showing `href` and text.
3. **task3.py** — Print all tags (counts, then flat listing in document order).
4. **task4.py** — Print all tags with an **id** attribute (single API call via `soup.select('[id]')`).
5. **task5.py** — Demonstrate `find_parent()`. You can pick a target via CSS (`--select`) and optionally restrict the parent tag name via `--parent`.
6. **task6.py** — Rewrite all `<b>` tags to `<blockquote>` and write `*.b_to_blockquote.html`.
7. **task7.py** — Add/replace `class="test"` on all `<p>` tags and write `*.p_class_test.html`.
8. **task8.py** — Extra API: remove `<script>/<style>` (decompose), unwrap `<span>`, print a text preview, write a cleaned file.

## Usage Examples
```bash
# 1) Prettify
python task1.py sample.html

# 2) All hyperlinks
python task2.py sample.html

# 3) All tags
python task3.py sample.html

# 4) Tags with id
python task4.py sample.html

# 5) find_parent examples
python task5.py sample.html --select "a" --parent "nav"
python task5.py sample.html --select "div.article-body a.read-more"

# 6) Convert <b> -> <blockquote>
python task6.py sample.html

# 7) Set class='test' on all <p>
python task7.py sample.html

# 8) Extra API usage
python task8.py sample.html
```

## Very Large File Note (GB‑scale)
These scripts **attempt** to process very large files, but full‑file parsing requires large memory and time.
- If your machine has insufficient RAM, parsing may fail or swap heavily.
- Prefer the `lxml` parser for speed and lower memory vs the built‑in `html.parser`.
- Run each command with `--time` to print elapsed time to stderr.

**Please record in this README (below) your actual observation** on a ~1 GB file:
- File: `<path and brief description>`
- Parser: `lxml | html.parser | xml`
- Result: `succeeded | failed (MemoryError) | took too long`
- Elapsed (from `--time` output): `X.XXX s`

## Observations (fill these in after your runs)
- [ ] File 1: ...
- [ ] File 2: ...
- [ ] File 3: ...
- ...
- [ ] 1 GB file: ...

## Notes
- BeautifulSoup’s method is `prettify()`, not `prettyfy()`.
- For XML inputs, use `--parser xml` to preserve XML semantics.
- For deeply nested structures, `task3.py` and `task5.py` are handy to explore parent/child relations.
