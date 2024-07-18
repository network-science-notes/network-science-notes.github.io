print("running precompilation script")

import shutil
import os
import nbformat as nb
import re

if not os.path.isdir("docs/live-notebooks"):
    os.makedirs("docs/live-notebooks", exist_ok=True)
    
if not os.path.isdir("chapters"):
    os.makedirs("chapters", exist_ok=True)

if "hidden" not in os.listdir("chapters"):
    source_dir = "source/hidden"
    destination_dir = "chapters/hidden"
    shutil.copytree(source_dir, destination_dir)

for f in os.listdir("source"):
    
    if f.endswith(".qmd"):
        with open(f"source/{f}", "r") as file: 
            cleaned = file.read().replace('#---\n', '')
            
            live_path = f"{f.replace('.qmd', '.ipynb')}"
            if live_path in os.listdir("docs/live-notebooks"):
                
                link_line = f"*Download the live notebook corresponding to these notes [here](../live-notebooks/{live_path}).* \n"
                
                cleaned_lines = cleaned.split("\n")
                ix = 0
                found = False
                while not found: 
                    line = cleaned_lines[ix]
                    if line: 
                        found = "#" in line 
                    ix += 1
                ix += 1    
                
                
                cleaned_lines.insert(ix, link_line)            
                cleaned = "\n".join(cleaned_lines)
            
            with open(f"chapters/{f}", "w") as new: 
                new.write(cleaned)
    
    elif f.endswith(".ipynb"):
        out_path = f"chapters/{f}"
        shutil.copyfile(f"source/{f}", out_path)   
        notebook = nb.read(out_path, as_version = 4)
        for cell in notebook["cells"]:
            cell["source"] = re.sub(r"#---\n", "", cell["source"])
            cell["source"] = re.sub(r"#---", "", cell["source"])

        nb.write(notebook, out_path)
            
        # os.system(f"quarto convert {f}")


