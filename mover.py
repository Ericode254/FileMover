import shutil
import os

def move(source: str, destination: str):
    for file_name in os.listdir(source):
        if file_name.endswith(".mp4") or file_name.endswith(".mkv"):
            shutil.move(source + "/" + file_name, destination)
            print("File(s) moved!!!")
            return

    print("No any video files present in the directory")

def main():
    source = input("Enter the source path of the files: ")
    destination = input("Enter the destination path of the files: ")

    if source == "" or destination == "":
        print("Enter source and destination")
        main()
    else:
        move(source, destination)

if __name__ == "__main__":
    main()

