from textnode import *
from htmlnode import *
from inline_markdown import * 

def main():
	text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
	print(text_to_textnodes(text))

if __name__=="__main__":
	main()
