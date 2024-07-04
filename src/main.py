from textnode import *
from htmlnode import *
from inline_markdown import split_nodes_delimiter

def main():
	node = TextNode("This **word** is bold, and so is this **one**", text_type_text)
	new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
	print(new_nodes)

if __name__=="__main__":
	main()
