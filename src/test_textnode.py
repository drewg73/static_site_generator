from io import StringIO
import unittest
from unittest.mock import patch

from textnode import *

class TestTextNodeEquals (unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", text_type_bold)
		node2 = TextNode("This is a text node", text_type_bold)
		self.assertEqual(node, node2)
	
	def test_eq_false_text(self):
		node = TextNode("This is a text node", text_type_text)
		node2 = TextNode("This is a text node", text_type_bold)
		self.assertNotEqual(node, node2)
	
	def test_eq_false_text_type(self):
		node = TextNode("This is a text node", text_type_text)
		node2 = TextNode("This is text node2", text_type_text)
		self.assertNotEqual(node, node2)
		
	def test_eq_url(self):
		node = TextNode("This is a text node", text_type_italic, "https://google.com")
		node2 = TextNode("This is a text node", text_type_italic, "https://google.com")
		self.assertEqual(node, node2)
		
	def test_repr_(self):
		text = "This is a text node"
		text_type = text_type_bold
		url = "https://google.com"
		expected = f'TextNode("{text}", "{text_type}", "{url}")\n'
		
		with patch('sys.stdout', new = StringIO()) as actual:
			print(TextNode(text, text_type, url))
			self.assertEqual(actual.getvalue(), expected)
		
if __name__ == "__main__":
	unittest.main()