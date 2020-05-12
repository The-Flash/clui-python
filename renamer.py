import pyfiglet # stylize text
import colorama
import argparse # parse command line options
import sys # used to exit program

from termcolor import cprint
from PyInquirer import prompt
from pathlib import Path

colorama.init()

# parsing command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", default="./", help="Directory to load files and folders from.") # directory to get list files/folders
args = vars(parser.parse_args())

NAME = "RENAMER"
CLOSING_REMARK = "THANKS FOR USING RENAMER"

def main():
    title = pyfiglet.figlet_format(NAME) # fancy title
    cprint(title, "green") # colored output: green
    directory = Path(args["directory"])
    directory_content = ({"name": str(f)} for f in directory.iterdir()) # generator expression for directory content(files/folders)

    question = [
        {
            "type": "checkbox",
            "name": "selected_files",
            "message": "Select files/folders to rename",
            "choices": directory_content
        }
    ]

    answer = prompt(question) # prompt user to answer question
    selected_files = answer.get("selected_files", None)
    if selected_files is None: # gracefully exit application if no options are selected
        sys.exit()

    for filename in selected_files: # loop through selected files/folders
        question = [
            {
                "type": "input",
                "name": "new_name",
                "message": "Rename ({}):".format(filename)
            }
        ]
        new_name = prompt(question).get("new_name", None) # prompt user to provide a new name for each
        if new_name is None or new_name == "": # check if no new name is provided
            continue # move to the next item in the list

        path = directory / filename # build file/folder path
        try:
            path.rename(new_name) # rename
        except FileExistsError: # check if file with that name already exists
            cprint("A file/folder with that name already exist", "red")
    
    closing_remark = pyfiglet.figlet_format(CLOSING_REMARK) # fancy text
    cprint(closing_remark, "green") # closing remark


if __name__ == "__main__":
    main()
