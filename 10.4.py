import os
import shutil
def copy_file_to_new_directory(src_file, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)  
    with open(src_file, 'r') as src:
        content = src.read()
    with open(os.path.join(dest_dir, os.path.basename(src_file)), 'w') as dest:
        dest.write(content)
    print(f"File copied to {dest_dir}")
src_file = 'example.txt'
dest_dir = 'new_subdir'
copy_file_to_new_directory(src_file, dest_dir)
