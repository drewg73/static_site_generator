from block_to_markdown import markdown_to_blocks
from markdown_to_html import *
import os

def extract_title(markdown):
	blocks = markdown_to_blocks(markdown)
	for block in blocks:
		if block.startswith("# "):
			return block[2:].strip()
		else:
			continue
	raise ValueError("No H1 heading found")

def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")
	try:
		from_file = open(from_path)
		markdown = from_file.read()
		from_file.close()
	except:
		print(f"{from_path} not found")
	try:
		template_file = open(template_path)
		template_html = template_file.read()
		template_file.close()
	except:
		print(f"{template_path} does not exist")

	html_node = markdown_to_html_node(markdown)
	content = html_node.to_html()
	title = extract_title(markdown)
	html = template_html.replace("{{ Title }}", title)
	html = html.replace("{{ Content }}", content)
	if not os.path.exists(dest_path):
		os.mkdir(dest_path)
	f = open(f"{dest_path}/index.html", "w")	
	f.write(html)
	f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	directory =	os.listdir(dir_path_content)
	for item in directory:
		if os.path.isfile(os.path.join(dir_path_content, item)):
			generate_page(os.path.join(dir_path_content, item), template_path, dest_dir_path)
			continue
		generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item))