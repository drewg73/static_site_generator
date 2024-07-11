from constants import *
from block_to_markdown import *

import unittest

class TestBlockToMarkdown(unittest.TestCase):
	def test_markdown_to_block(self):
		markdown = "This is some text\n\nThis is more text\nFollowed by more\n\nHere is some **bold** text"
		expected = [
			"This is some text",
			"This is more text\nFollowed by more",
			"Here is some **bold** text",
		]
		actual = markdown_to_blocks(markdown)
		self.assertListEqual(actual, expected)
	
	def test_starting_with_new_line(self):
		markdown = "\nText starting with new line"
		expected = ["Text starting with new line"]
		actual = markdown_to_blocks(markdown)
		self.assertListEqual(actual, expected)

	def test_multiple_spaces_at_begining_and_end(self):
		markdown = "  spaces before and after "
		expected = ["spaces before and after"]
		actual = markdown_to_blocks(markdown)
		self.assertListEqual(actual, expected)

	def test_consecutive_empty_lines(self):
		markdown = "# This is a heading\n\n\nThis is a paragraph\n\n\n* This is a list item"
		expected = [
			"# This is a heading",
			"This is a paragraph",
			"* This is a list item",
		]
		actual = markdown_to_blocks(markdown)
		self.assertListEqual(actual, expected)

	def test_empty_text(self):
		markdown = ""
		expected = []
		actual = markdown_to_blocks(markdown)
		self.assertListEqual(actual, expected)

	def test_one_large_block(self):
		markdown = "Line one\nLine two\nLine three\nLine four"
		expected = [
			"Line one\nLine two\nLine three\nLine four",
		]
		actual = markdown_to_blocks(markdown)
		self.assertListEqual(actual, expected)

	def test_block_type_heading(self):
		actual = []
		expected = []
		for i in range(1, 7):
			actual.append(block_to_block_type(f'{"#"*i} Heading'))
			expected.append(BLOCK_TYPE_HEADING)
		self.assertListEqual(actual, expected)

	def test_block_type_code(self):
		block = "```let y = 0```"
		expected = BLOCK_TYPE_CODE
		actual = block_to_block_type(block)
		self.assertEqual(actual, expected)

	def test_opening_backticks(self):
		block = "``` this isn't code"
		expected = BLOCK_TYPE_PARAGRAPH
		actual = block_to_block_type(block)
		self.assertEqual(actual, expected)

	def test_block_type_quote(self):
		block = "> This is how democracy dies\n> With thunderous applause"
		expected = BLOCK_TYPE_QUOTE
		actual = block_to_block_type(block)
		self.assertEqual(actual, expected)

	def test_line_missing_cheveron(self):
		block = "> Line one\nLine two\n> Line three"
		expected = BLOCK_TYPE_PARAGRAPH
		actual = block_to_block_type(block)
		self.assertEqual(actual, expected)

	def test_unordered_list_hyphen(self):
		block = "- item one\n- item two\n- item three"
		expected = BLOCK_TYPE_UNORDERED_LIST
		actual = block_to_block_type(block)
		self.assertEqual(actual, expected)

	def test_unordered_list_asterisk(self):
		block = "* item one\n* item two\n* item three"
		expected = BLOCK_TYPE_UNORDERED_LIST
		actual = block_to_block_type(block)
		self.assertEqual(actual, expected)

	def test_hyphe_and_asterisk(self):
		block = "* item one\n- item two\n* item three"
		expected = BLOCK_TYPE_PARAGRAPH
		actual = block_to_block_type(block)
		self.assertEqual(actual, expected)

	def test_ordered_list(self):
		block = "1. item one\n2. item two\n3. item three"
		expected = BLOCK_TYPE_ORDERED_LIST
		actual = block_to_block_type(block)
		self.assertEqual(actual, expected)

	def test_out_of_order_list(self):
		block = "3. item one\n2. item two\n3. item three"
		expected = BLOCK_TYPE_PARAGRAPH
		actual = block_to_block_type(block)
		self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()