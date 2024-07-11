import os
import shutil

def clear_directory(target):
	files = os.listdir(target)
	if len(files) == 0:
		return
	for file in files:
		path = os.path.join(target, file)
		if os.path.isfile(path):
			os.remove(path)
		else:
			shutil.rmtree(path)
	return


def copy_and_move_files(source, target):
	if not os.path.exists(source):
		raise ValueError(f"{source} does not exist")
	if not os.path.exists(target):
		raise ValueError(f"{target} does not exist")
	print(f"clearing {target}")
	clear_directory(target)
	if os.path.isfile(source):
		print(f"Adding {source} to {target}")
		shutil.copy(source, target)
		return
	directory = os.listdir(source)
	for item in directory:
		current_path = os.path.join(source, item)
		if os.path.isfile(current_path):
			print(f"adding {item} to {target}")
			shutil.copy(current_path, target)
		else:
			print(f"creating directory {item} in {target}")
			os.mkdir(os.path.join(target, item))
			copy_and_move_files(current_path, os.path.join(target, item))

def main():
	source_dir = "./static"
	target_dir = "./public"
	copy_and_move_files(source_dir, target_dir)

if __name__=="__main__":
	main()
