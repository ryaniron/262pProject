# Milestone-4
This enables elegant tree-walking APIs without requiring calls to .descendants, .contents, or .find_all().

Design Choice
BeautifulSoup structures its DOM as a tree of Tag and NavigableString nodes. Making the root BeautifulSoup object iterable requires a traversal mechanism that:
- Works on all node types
- Avoids recursion (deep documents risk recursion depth errors)
- Does not materialize a node list in memory
- Preserves document order
- Operates lazily

I selected an iterative depth-first traversal using a stack, a standard approach for efficient generator-based tree iteration.

Alternative Considered
- Using .descendants would be an easy shortcut, but is disallowed:
    - It internally builds lists in some cases
    - It performs recursion
    - It does not give full control over traversal order
    - It violates the milestone requirement to implement iteration independently

Recommendation
- This feature significantly improves the usability of BeautifulSoup for tree analysis, transformations, and debugging. It is consistent with Pythonic design and complements existing traversal helpers.
- I recommend integrating this into the core library:
- It offers no backwards incompatibility
- It provides a simple, intuitive API
- It improves performance over .find_all() for full-tree scans
- Users expect containers to be iterable

Conclusion
- This milestone enhances BeautifulSoup by adding a clean, efficient iterator that produces nodes in document order without building extra structures. The implementation is compact, non-disruptive, and practically useful for many workflows.