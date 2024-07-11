from textnode import *
from inline_markdown import *
from constants import *
from block_to_markdown import *
from htmlnode import *

def markdown_to_html_node(markdown):
	blocks = markdown_to_blocks(markdown)
	children = []
	for block in blocks:
		html_node = block_to_html_node(block)
		children.append(html_node)
	return ParentNode("div", children)

def block_to_html_node(block):
	block_type = block_to_block_type(block)
	if block_type == BLOCK_TYPE_PARAGRAPH:
		return paragraph_to_html_node(block)	
	if block_type == BLOCK_TYPE_HEADING:
		return headings_to_html_node(block)
	if block_type == BLOCK_TYPE_CODE:
		return code_to_html(block)
	if block_type == BLOCK_TYPE_ORDERED_LIST:
		return ordered_list_to_html(block)
	if block_type == BLOCK_TYPE_UNORDERED_LIST:
		return unordered_list_to_html(block)
	if block_type == BLOCK_TYPE_QUOTE:
		return quote_to_html(block)
	raise ValueError("Invalid block type")

def text_to_children(text):
	text_nodes = text_to_textnodes(text)
	children = []
	for text_node in text_nodes:
		html_node = text_node_to_html_node(text_node)
		children.append(html_node)
	return children

def paragraph_to_html_node(block):
	lines = block.split("\n")
	paragraph = " ".join(lines)
	children = text_to_children(paragraph)
	return ParentNode("p", children)

def headings_to_html_node(block):
	heading_level = 0
	for char in block:
		if char == "#":
			heading_level += 1
		else:
			break
	if heading_level + 1 > len(block):
		raise ValueError(f"Invalid heading level: {heading_level}")
	text = block[heading_level + 1:]
	children = text_to_children(text)
	return ParentNode(f"h{heading_level}", children)

def code_to_html(block):
	if not block.startswith("```") or not block.endswith("```"):
		raise ValueError("Invalid code block")
	text = block[4:-4]
	children = text_to_children(text)
	code = ParentNode("code", children)
	return ParentNode("pre", [code])

def ordered_list_to_html(block):
	list_items = block.split("\n")
	html_list_items = []
	for list_item in list_items:
		text = list_item[3:]
		children = text_to_children(text)
		html_list_items.append(ParentNode("li", children))
	return ParentNode("ol", html_list_items)

def unordered_list_to_html(block):
	list_items = block.split("\n")
	html_list_items = []
	for list_item in list_items:
		text = list_item[2:]
		children = text_to_children(text)
		html_list_items.append(ParentNode("li", children))
	return ParentNode("ul", html_list_items)

def quote_to_html(block):
	lines = block.split("\n")
	new_lines = []
	for line in lines:
		if not line.startswith(">"):
			raise ValueError("Invalid quote block")
		new_lines.append(line.lstrip(">").strip())
	text = " ".join(new_lines)
	children = text_to_children(text)
	return ParentNode("blockquote", children)