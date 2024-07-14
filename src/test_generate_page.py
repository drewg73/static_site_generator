from generate_page import *
import unittest

class TestGeneratePate(unittest.TestCase):
	def test_extract_title(self):
		markdown = "# Heading 1"
		actual = extract_title(markdown)
		expected = "Heading 1"
		self.assertEqual(actual, expected)

	def test_h1_not_at_top(self):
		markdown = "this is line one\n\n# This is the Heading\n\nthis is the third line"
		actual = extract_title(markdown)
		expected = "This is the Heading"
		self.assertEqual(actual, expected)

	def test_different_heading(self):
		with self.assertRaises(ValueError) as context:
			extract_title("## Heading 2")
		self.assertTrue("No H1 heading found", context.exception)

if __name__ == "__main__":
	unittest.main()
