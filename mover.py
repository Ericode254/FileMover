import shutil

def move(source: str, destination: str):
    sources = []

    with open("text.txt", "r") as file:
        for f in file.readlines():
            sources.append(f)

    for i in sources:
        shutil.move(source + "/" + i.rstrip("\n"), destination)

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

