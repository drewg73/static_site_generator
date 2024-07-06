from textnode import *
from htmlnode import *
from inline_markdown import * 

def main():
	node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
	)
	new_nodes = split_nodes_image([node])
	print(new_nodes)

if __name__=="__main__":
	main()
