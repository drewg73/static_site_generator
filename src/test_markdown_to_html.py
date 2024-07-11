from markdown_to_html import *
from htmlnode import *

import unittest

class TestMarkdownToHTML(unittest.TestCase):
	def test_headings(self):
		actual_headings = []
		expected_headings = []
		for level in range(1, 7):
			md = f"{'#'*level} Heading {level}"
			node = markdown_to_html_node(md)
			actual_headings.append(node.to_html())
			expected_headings.append(f"<div><h{level}>Heading {level}</h{level}></div>")
		self.assertListEqual(actual_headings, expected_headings)

	def test_paragraph(self):
		md = """**This is bold** followed by some *italic*
[link](https://google.com)
![image](https://google.com)
		"""
		node = markdown_to_html_node(md)
		actual = node.to_html()
		expected = '<div><p><b>This is bold</b> followed by some <i>italic</i> <a href="https://google.com">link</a> <img src="https://google.com" alt="image"></img></p></div>'
		self.assertEqual(actual, expected)

	def test_code(self):
		md = """```
var x = 0
```"""
		node = markdown_to_html_node(md)
		actual = node.to_html()
		expected = "<div><pre><code>var x = 0</code></pre></div>"
		self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()