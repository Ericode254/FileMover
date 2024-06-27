# FILE MOVER
File Mover is a simple command line application that can be used to move files around on your machine,
with added features like choosing the type of files to move and the number of files to move. The application
is able to get your home path so you don't need to provide the complete paths.

## Requirements
In order to run the application first you need `python` installed on your machine.
Modules needed: - argparse
                - os
                - shutil
                - sys

## Installation
`python -r install requirements.txt` - To install all the modules needed.
`python mover.py` - To run the application.

## Moving files listed in a file
`python mover.py --file <file_name>` - <file_name> represents the name of the file containing the file names.

