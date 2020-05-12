import argparse

parser = argparse.ArgumentParser(description="CodeWithFlash: Argparse Basic Usage")
parser.add_argument("name")
parser.add_argument("-a", "--age")

args = vars(parser.parse_args()) # get a dictionary representation
print("Value of args", args)
name = args["name"]
age = args["age"]

print("Name:", name, "Age:", age)