def markdown_to_blocks(markdown):
  blocks = []
  block = ""
  for line in markdown.splitlines():
    # If the current line and the block are empty, a empty line was encountered.
    # Continue the loop
    if not line and not block:
      continue
    # If the current line is empty and the block isn't, a new line was encountered.
    # Start a new block, by appendign block to blocks and clearing block.
    if not line and block:
      blocks.append(block.strip())
      block = ""
      continue
    # If neither of the above conditions are true, then we are on a current block.
    # Append the line to the block
    block += (f"{line}\n")
  if block:
    # Cleaning up if block is not empty.
    blocks.append(block.strip())
  return blocks

def block_to_block_type(block):
  if re.match(r"^#+ ", block):
    return BLOCK_TYPE_HEADING
  if block.startswith("```") and block.endswith("```"):
    return BLOCK_TYPE_CODE
  if len(re.findall(r"> ", block)) == len(block.split("\n")):
    return BLOCK_TYPE_QUOTE
  if len(re.findall(r"\* ", block)) == len(block.split("\n")):
    return BLOCK_TYPE_UNORDERED_LIST
  if len(re.findall(r"- ", block)) == len(block.split("\n")):
    return BLOCK_TYPE_UNORDERED_LIST
  
  is_list = True
  for i in range(len(block.split("\n"))):
    pattern = re.compile(f'{i}/. ')
    if pattern.match is None:
      is_list = False
      break
  if is_list:
    return BLOCK_TYPE_ORDERED_LIST
  
  return BLOCK_TYPE_PARAGRAPH
