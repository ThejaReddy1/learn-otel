import os
import shutil
import glob

repo_root = r"d:\OTelInstrumentation"
site_dir = os.path.join(repo_root, "site")

if not os.path.exists(site_dir):
    os.makedirs(site_dir)

files_to_move = glob.glob(os.path.join(repo_root, "day-*.html"))
files_to_move.append(os.path.join(repo_root, "quick-start.html"))
dirs_to_move = ["css", "js"]

for f in files_to_move:
    if os.path.exists(f):
        shutil.move(f, site_dir)

for d in dirs_to_move:
    src = os.path.join(repo_root, d)
    if os.path.exists(src):
        dst = os.path.join(site_dir, d)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.move(src, site_dir)

# Update root index.html
index_file = os.path.join(repo_root, "index.html")
if os.path.exists(index_file):
    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Avoid double replacing if already site/css
    content = content.replace('href="site/css/', 'href="css/') 
    content = content.replace('href="site/day-', 'href="day-')
    content = content.replace('href="site/quick-start.html"', 'href="quick-start.html"')
    content = content.replace('src="site/js/', 'src="js/')

    content = content.replace('href="css/', 'href="site/css/')
    content = content.replace('href="day-', 'href="site/day-')
    content = content.replace('href="quick-start.html"', 'href="site/quick-start.html"')
    content = content.replace('src="js/', 'src="site/js/')

    with open(index_file, "w", encoding="utf-8") as f:
        f.write(content)

# Update site HTML files
site_html_files = glob.glob(os.path.join(site_dir, "*.html"))
for f in site_html_files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    content = content.replace('href="../index.html"', 'href="index.html"')
    content = content.replace('href="index.html"', 'href="../index.html"')

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Reverted to site/ layout with index in root.")
