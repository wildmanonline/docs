#!/usr/bin/env python
import os
import sys
import re
import frontmatter
import textwrap

DOCS_DIR = [
    "docs/guides",
    "docs/products",
    "docs/bundles",
    "docs/assets",
    "docs/api",
    "docs/reference-architecture",
    "docs/release-notes"
]

# ------------------
# Parses through each file and, if that file contains an h1_title, updates it
# to use the new title_meta parameter instead.
# ------------------
def update_titles():

    # Iterate through each file in each docs directory
    for dir in DOCS_DIR:
        for root, dirs, files in os.walk(dir):
            for file in files:

                # The relative file path of the file
                file_path = os.path.join(root, file)
                path_segments = file_path.split("/")

                # If the file is markdown...
                if file.endswith('.md'):

                    with open(file_path, "r") as fp:
                        lines = fp.readlines()

                    line_num_title = 0
                    line_num_title_meta = 0
                    line_num_h1_title = 0
                    line_num_enable_h1 = 0

                    title = ""
                    title_meta = ""
                    h1_title = ""

                    inside_frontmatter = False
                    update = False
                    duplicate_title = False

                    # Iterates through each line of the file and locates
                    # the title and h1_title parameters.
                    for i, line in enumerate(lines):
                        if line.startswith("---") and not inside_frontmatter:
                            inside_frontmatter = True
                        elif line.startswith("---") and inside_frontmatter:
                            inside_frontmatter = False

                        if inside_frontmatter == False:
                            continue

                        if line.startswith("title:"):
                            title = line
                            line_num_title = i
                        elif line.startswith("title_meta:"):
                            title_meta = line
                            line_num_title_meta = i
                        elif line.startswith("h1_title:"):
                            h1_title = line
                            line_num_h1_title = i

                    # Update title if h1_tile exists
                    if not h1_title == "":
                        title_meta = title.replace("title:", "title_meta:")
                        title = h1_title.replace("h1_title:", "title:")
                        update = True

                    # If the there is no h1_title, go to the next file.
                    if not update:
                        continue

                    # Determine if title and title_meta are duplicates
                    if title.replace("title:","") == title_meta.replace("title_meta:",""):
                        duplicate_title = True

                    # Write to the file
                    with open(file_path, "w") as fp:
                        for line in lines:

                            if line.startswith("---") and not inside_frontmatter:
                                inside_frontmatter = True
                            elif line.startswith("---") and inside_frontmatter:
                                inside_frontmatter = False

                            if inside_frontmatter:
                                if line.startswith("title:") and duplicate_title:
                                    fp.write(title)
                                elif line.startswith("title:") and not duplicate_title:
                                    fp.write(title)
                                    fp.write(title_meta)
                                elif not line.startswith("h1_title:") and not line.startswith("enable_h1:"):
                                    fp.write(line)
                            else:
                                fp.write(line)

# ------------------
# Main function
# ------------------
def main():

    update_titles()

if __name__ == "__main__":
    main()