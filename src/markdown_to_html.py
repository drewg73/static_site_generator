from textnode import *
from inline_markdown import *
from constants import *
from block_to_markdown import *
from htmlnode import *

def markdown_to_html_node(markdown):
	html_nodes = []
	blocks = markdown_to_blocks(markdown)
	for block in blocks:
		block_type = block_to_block_type(block)
		if block_type == BLOCK_TYPE_PARAGRAPH