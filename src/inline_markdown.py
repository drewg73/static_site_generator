from textnode import (
	TextNode,
	text_type_text,
	text_type_italic,
	text_type_bold,
	text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	# list for holding processed TextNodes
	new_nodes = []
	for old_node in old_nodes:
		if old_node.text_type != text_type_text:
			new_nodes.append(old_Node)
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