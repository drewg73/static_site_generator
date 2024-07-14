from textnode import (
	TextNode,
	text_type_text,
	text_type_italic,
	text_type_bold,
	text_type_code,
	text_type_image,
	text_type_link,
)

import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	# list for holding processed TextNodes
	new_nodes = []
	for old_node in old_nodes:
		if old_node.text_type != text_type_text:
			new_nodes.append(old_node)
			continue
		sections = old_node.text.split(delimiter)
		if len(sections) %2 == 0:
			raise ValueError("Invalid markdown, formatted section not closed")
		for i in range(len(sections)):
			if sections[i] == "":
				continue
			if i % 2 == 0:
				new_nodes.append(TextNode(sections[i], text_type_text))
			else:
				new_nodes.append(TextNode(sections[i], text_type))
	return new_nodes

def extract_markdown_images(text):
	matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
	return matches

def split_nodes_image(old_nodes):
	new_nodes = []
	for node in old_nodes:
		images = extract_markdown_images(node.text)
		if not images:
			new_nodes.append(node)
			continue
		text_to_process = node.text
		for image_tup in images:
			split_parts = text_to_process.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
			if split_parts[0]:
				new_nodes.append(TextNode(split_parts[0], text_type_text))
			new_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
			text_to_process = split_parts[1]
		if text_to_process:
			new_nodes.append(TextNode(text_to_process, text_type_text))
	return new_nodes

def extract_markdown_links(text):
	matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
	return matches

def split_nodes_link(old_nodes):
	new_nodes = []
	for node in old_nodes:
		links = extract_markdown_links(node.text)
		if not links:
			new_nodes.append(node)
			continue
		text_to_process = node.text
		for link_tup in links:
			split_parts = text_to_process.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
			if split_parts[0]:
				new_nodes.append(TextNode(split_parts[0], text_type_text))
			new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
			text_to_process = split_parts[1]
		if text_to_process:
			new_nodes.append(TextNode(text_to_process, text_type_text))
	return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "_", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes