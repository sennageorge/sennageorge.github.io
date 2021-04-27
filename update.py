import re
import os
import sys
import subprocess

from bs4 import BeautifulSoup
from datetime import datetime

from templates.project_description import project_description_template
from templates.project_thumbnail import project_thumbnail_template

portfolio_dir: str = 'assets/img/portfolio'

"""
Title:
Subtitle:
Category:
Description:
Image:
"""

def main() -> None:
    new_files: str = subprocess.check_output("git status", shell=True).decode()
    new_files = [new_file.strip() for new_file in new_files.split("\n")[5:-3] if '.txt' in new_file]

    fields: list = ["Title", "Subtitle", "Category", "Description", "Image"]

    for new_file in new_files:
        info: dict = dict()
        with open(new_file, 'r') as f:
            content: str = f.read()
            splices: list = list()

            for field in fields:
                splices.append(content.find(field + ":"))
                if splices[-1] == -1:
                    raise Exception(f"Error: Did not supply {field}")

            for i in range(len(fields) - 1):
                value = content[splices[i] + len(fields[i]) + 1: splices[i + 1]]
                value = value.strip()
                info[fields[i]] = value

            info["Image"] = content[splices[-1] + len(fields[-1]) + 1:].strip()
            info["Date"] = datetime.now().strftime("%B") + " " + str(datetime.now().year)

        page_src: list = list()

        with open('index.html', 'r') as f:
            page_src: list = f.readlines()

        soup: BeautifulSoup = BeautifulSoup("".join(page_src), features='html.parser')

        project_descriptions: list = soup.findAll("div", {"id": re.compile(r"portfolioModal.*")})

        new_id: str = "1"
        if len(project_descriptions) > 0:
            new_id: str = str(int(project_descriptions[-1].get("id")[len("portfolioModal"):]) + 1)



        thumbnail_idx: int = 0

        for i, line in enumerate(page_src):
            if "section" in line and "id=\"portfolio\"" in line:
                for j in range(i + 1, len(page_src)):
                    if "</section>" in page_src[j]:
                        thumbnail_idx = j - 2
                        break
                break

        description_index: int = 0
        for i, line in enumerate(reversed(page_src)):
            if "</div>" in line:
                description_index = -i
                break

        page_src.insert(thumbnail_idx, project_thumbnail_template.format(new_id,
                                                                         info["Image"],
                                                                         info["Title"],
                                                                         info["Subtitle"]))

        page_src.insert(description_index, project_description_template.format(new_id,
                                                        info["Title"],
                                                        info["Subtitle"],
                                                        info["Image"],
                                                        info["Description"],
                                                        info["Date"],
                                                        info["Category"]))

        with open('index.html', 'w') as f:
            f.write("".join(page_src))



        os.system("git add --all; git commit -m 'update'; git push -f origin main")

    return 0

if __name__ == "__main__":
    sys.exit(main())