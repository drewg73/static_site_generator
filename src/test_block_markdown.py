import unittest
from block_markdown import markdown_to_blocks

class TestMarkdownToBlock(unittest.TestCase):
    def test_markdown_to_block(self):
        text = "This is some text\n\nThis is more text\nFollowed by more\n\nHere is some with **bold** text"
        expected = [
            "This is some text",
            "This is more text\nFollowed by more",
            "Here is some with **bold** text"
        ]
        actual = markdown_to_blocks(text)
        self.assertListEqual(actual, expected)
    
    def test_starting_with_new_line(self):
         text = "\ntext starting with new line\n\nHere is some more\nfollowed by more"
         expected = [
              "text starting with new line",
              "Here is some more\nfollowed by more"
         ]
         actual = (markdown_to_blocks(text))
         self.assertListEqual(actual, expected)

    def test_multiple_spaces_at_begining_and_end(self):
         text = "      wow, that's a lot of space     "
         expected = ["wow, that's a lot of space"]
         actual = markdown_to_blocks(text)
         self.assertListEqual(actual, expected)
	    
    def test_consecutive_empty_lines(self):
         text = "# This is a heading\n\n\nThis is a paragraph.\n\n\n* This is a list item"
         expected = [
              "# This is a heading",
              "This is a paragraph.",
              "* This is a list item"
         ]
         actual = markdown_to_blocks(text)
         self.assertListEqual(actual, expected)

    def test_empty_text(self):
        text = ""
        expected = []
        actual = markdown_to_blocks(text)
        self.assertListEqual(actual, expected)

    def test_one_large_block(self):
        text = "Line one\nLine two\nLine three\nLine four"
        expected = [
           "Line one\nLine two\nLine three\nLine four"
        ]
        actual = markdown_to_blocks(text)
        self.assertListEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()
