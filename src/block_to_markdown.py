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
      block.append(block.strip())
      block = ""
      continue
    # If neither of the above conditions are true, then we are on a current block.
    # Append the line to the block
    block += (f"{line}\n")
  if block:
    # Cleaning up if block is not empty.
    blocks.append(block.strip())
  return blocks
