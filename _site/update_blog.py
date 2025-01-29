import os
import shutil
import re
from datetime import datetime

# Define paths
obsidian_blog_path = "//mnt/c/Users/matt/Documents/Stratotanker/BlogPosts/"
obsidian_media_path = "//mnt/c/Users/matt/Documents/Stratotanker/media"
jekyll_posts_path = "_posts"
jekyll_images_path = "assets/images"

# Function to extract image references from Markdown and replace their format
def process_markdown(file_path, output_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Find all image references in the format ![[image_name.png]]
    image_references = re.findall(r"!\[\[(.+?)\]\]", content)

    # Replace image references with Jekyll-friendly format ![blah](image_name.png)
    updated_content = re.sub(r"!\[\[(.+?)\]\]", r"![blah](/assets/images/\1)", content)

    # Save the updated content to the new location
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

    return image_references

# Copy markdown files and process images
for filename in os.listdir(obsidian_blog_path):
    if filename.endswith(".md"):
        # Generate a Jekyll-friendly filename: YYYY-MM-DD-title.md
        title = filename.replace(" ", "-").replace(".md", "")
        today = datetime.today().strftime('%Y-%m-%d')
        new_filename = f"{today}-{title}.md"
        source_path = os.path.join(obsidian_blog_path, filename)
        destination_path = os.path.join(jekyll_posts_path, new_filename)

        # Process the markdown file and get the image references
        referenced_images = process_markdown(source_path, destination_path)
        print(f"Copied and processed: {filename} -> {new_filename}")

        # Copy referenced images to Jekyll `assets/images`
        for image_name in referenced_images:
            source_image_path = os.path.join(obsidian_media_path, image_name)
            destination_image_path = os.path.join(jekyll_images_path, image_name)

            if os.path.exists(source_image_path):
                shutil.copy(source_image_path, destination_image_path)
                print(f"Copied image: {image_name}")
            else:
                print(f"Image not found: {image_name}")

# Automate Git commands
#os.chdir("path/to/Jekyll")
#os.system("git add .")
#os.system("git commit -m 'Update blog content'")
#os.system("git push")
#print("Blog updated and pushed to GitHub Pages!")
