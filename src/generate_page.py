from block_to_markdown import markdown_to_blocks

def extract_title(markdown):
	blocks = markdown_to_blocks(markdown)
	for block in blocks:
		if block.startswith("# "):
			return block[2:].strip()
		else:
			continue
	raise ValueError("No H1 heading found")