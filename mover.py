import shutil
import os
import sys
import argparse


# responsible for checking the type of system
def sys_check() -> str:
    if sys.platform != "win32":
        sys_path = "/home/code/"
        return sys_path
    else:
        sys_path = r"C:\\users\code"
        return sys_path

# the root directory
sys_path = sys_check()

# checking whether a specific directory exists
def directory_validity(path: str) -> bool:
    for folder_name in os.listdir(sys_path):
        if folder_name == path:
            return True

    return False


# is responsible for creating the directory if not present
def destination_creation(name: str):
    if directory_validity(name) is False:
        os.mkdir(sys_path + name)
        return


# is responsible for moving the files to the specified directory
def move(source: str, destination: str, file: tuple[str]):
    destination_creation(destination)
    if directory_validity(source) is True:
        for file_name in os.listdir(sys_path + source):
            if file_name.endswith(file):
                shutil.move(sys_path + source + "/" + file_name, sys_path + destination)
            elif file_name.endswith(file) is False:
                print("The files stated are not present")
    else:
        print("Enter the correct source")


# responsible for moving files from a list
def move_from_file(source: str, destination: str, file: list[str]):
    destination_creation(destination)
    if directory_validity(source) is True:
        for file_name in os.listdir(sys_path + source):
            if file_name in file:
                shutil.move(sys_path + source + "/" + file_name, sys_path + destination)
            elif file_name not in file:
                print("Files not present")
    else:
        print("Enter the correct source")


# responsible for taking a list as a command line argument
def parse_list_to_move() -> list[str]:
    parser = argparse.ArgumentParser(description="Reads from file")
    parser.add_argument("--file",
                        default=sys.stdin,
                        type=argparse.FileType("r"),
                        help="python mover.py --file <file name>")
    args = parser.parse_args()
    file_names = []
    for line in args.name.readlines():
        line = line.rstrip("\n")
        file_names.append(line)

    return file_names


# handles the execution
def main():
    print(
        """
                ###################### #####                #####
                ###                    ###  #              #  ###
                ###                    ###   #            #   ###
                ###                    ###    #          #    ###
                ###################### ###     #       #      ###
                ###                    ###      #    #        ###
                ###                    ###       ###          ###
                ###                    ###                    ###
                ###                    ###                    ###
                ###                    ###                    ###
        """
    )

    choices = {
        "1" : [".txt"],
        "2" : [".mp4", ".mkv"],
        "3" : [".doc", ".docx", ".pdf", ".pptx"],
        "4" : [".jpg", ".jpeg", ".png"]
    }

    source = input("Enter the source path of the files: ")
    destination = input("Enter the destination path of the files: ")
    print("What type of file(s) would you like to move?")
    print("""
             1.  Text files (txt)
             2.  Video files (mp4, mkv)
             3.  Documents (doc, docx, pdf)
             4.  Pictures (jpg, jpeg, png)
          """
        )

    choice = input("Enter your choice: ")
    if choice in choices:
        if source == "" :
            print("Enter source!")
            main()
        elif destination == "":
            print("Enter the destination")
            main()
        else:
            file1 = parse_list_to_move()
            if not file1:
                file2 = tuple(choices[choice])
                move(source, destination, file2)
                print("File(s) moved!!!")
            else:
                move_from_file(source, destination, file1)
    else:
        print("Wrong choice")
        trial = input("Would you like to try again (t) or quit (q) (t | q): ")
        if trial == "t":
            main()
        else:
            print("Bye!!!")

if __name__ == "__main__":
    main()
