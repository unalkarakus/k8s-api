import os

path = os.environ.get('LOG_PATH')

if path is None or path == "":
    path = "current.txt"

def write_to_file(data):
    with open(path, "a") as file:
        file.write(data)

def read_from_file():
    with open(path, "r") as file:
        return file.read()
            