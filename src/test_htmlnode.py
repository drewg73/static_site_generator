from io import StringIO
import unittest
from unittest.mock import patch

from htmlnode import *

class TestHTMLNode (unittest.TestCase):
	def test_props_to_html(self):
		node = HTMLNode(
			None,
			None,
			None,
			{
				"href": "https://google.com",
				"target": "_blank"
			}
		)
		expected = ' href="https://google.com" target="_blank"'	
		self.assertEqual(node.props_to_html(), expected)
	
	def test_props_to_html_with_no_props(self):
		node = HTMLNode(None, None, None, None)
		expected = ""
		self.assertEqual(node.props_to_html(), expected)
		
	def test_to_html_no_children(self):
		node = LeafNode("p", "Hello, World!")
		actual = node.to_html()
		expected = "<p>Hello, World!</p>"
		self.assertEqual(actual, expected)
		
	def test_to_html_no_tag(self):
		node = LeafNode(None, "Hello, World!")
		actual = node.to_html()
		expected = "Hello, World!"
		self.assertEqual(actual, expected)
		
	def test_to_html_with_props(self):
		node = LeafNode("a", "Click Me", {"href": "https://google.com", "target": "_blank"})
		actual = node.to_html()
		expected = '<a href="https://google.com" target="_blank">Click Me</a>'
		self.assertEqual(actual, expected)

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		actual = parent_node.to_html()
		expected = "<div><span>child</span></div>"
		self.assertEqual(actual, expected)

	def test_to_html_with_grandchildren(self):
		grandchild = LeafNode("b", "grandchild")
		child = ParentNode("span", [grandchild])
		parent = ParentNode("div", [child])
		actual = parent.to_html()
		expected = "<div><span><b>grandchild</b></span></div>"
		self.assertEqual(actual, expected)

	def test_to_html_many_children(self):
		node = ParentNode(
			"div",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			]
		)
		actual = node.to_html()
		expected = "<div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div>"

	def test_repr_(self):
		tag = "a"
		value = "This is an anchor tag"
		children = None
		props = {"href": "https://google.com", "target": "_blank"}
		expected = f'HTMLNode(<{tag}>, "{value}", children: {children}, {props})\n'
		with patch('sys.stdout', new = StringIO()) as actual:
			print(HTMLNode(tag, value, children, props))
			self.assertEqual(actual.getvalue(), expected)

if __name__ == "__main__":
	unittest.main()