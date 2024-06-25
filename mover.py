import shutil
import os

# is responsible for moving the files to the specified directory
def move(source: str, destination: str, file: tuple[str]):
    for file_name in os.listdir(source):
        if file_name.endswith(file):
            shutil.move(source + "/" + file_name, destination)
        else:
            print("The files stated are not present")

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
        "3" : [".doc", ".docx", ".pdf"],
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
    if choice in choices.keys():
        if source == "" :
            print("Enter source!")
            main()
        elif destination == "":
            print("Enter the destination")
            main()
        else:
            file = tuple(choices[choice])
            move(source, destination, file)
            print("File(s) moved!!!")
    else:
        print("Wrong choice")
        trial = input("Would you like to try again (t) or quit (q) (t | q): ")
        if trial == "t":
            main()
        else:
            print("Bye!!!")

if __name__ == "__main__":
    main()

