from textnode import *
from htmlnode import *
from inline_markdown import * 

def main():
	text = "This is text with an [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
	print(extract_markdown_links(text))

if __name__=="__main__":
	main()
