import shutil
import os
import re

# https://stackoverflow.com/questions/12683834/how-to-copy-directory-recursively-in-python-and-overwrite-all

def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

if not os.path.isdir("docs/full-notes"):
    os.makedirs("docs/full-notes", exist_ok=True)
    
for f in os.listdir("docs/chapters"):
    if f.endswith(".html"):
        with open(f"docs/chapters/{f}", "r") as file: 
            html = file.read()
        
        regex = r'<div class=[\S\s]*?hide[\S\s]*?">[\S\s]*?</div>'
        cleaned = re.sub(regex, "", html)
        
        with open(f"docs/full-notes/{f}", "w") as new:
            new.write(html)
        
        with open(f"docs/chapters/{f}", "w") as file: 
            file.write(cleaned)
            
    else:
        out_path = f"docs/full-notes/{f}"
        copy_and_overwrite(f"docs/chapters/{f}", out_path)
        