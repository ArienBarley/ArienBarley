import os
import json
output = 'filetree.json'
ignore = '.DS_Store'

tree = {}
for root, dirs, files in os.walk("."):
    # skip ignored folders
    dirs[:] = [d for d in dirs if d not in ignore]
    
    # clean up the path (removes leading ./)
    clean_root = root.lstrip("./").lstrip("\\") or "root"
    
    if files:
        tree[clean_root] = files



print("----")
for item in tree: 
	print(item, " : ", tree[item])

with open(output, "w") as f: 
	json.dump(tree, f, indent = 2)


print('done')