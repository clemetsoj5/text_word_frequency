
from tkinter.filedialog import *
import re

def open_and_read_file():
    # Have user select file to open
    path = askopenfilename()
    # Open the file and remove all the line endings as well as any non alpha numeric characters
    # besides space characters
    with open(path, 'r') as file:
        data = file.read().replace('\n', '')
        data = re.sub(r'[^a-zA-Z0-9\s]', '', data)
    # return the full text as a complete string
    return(data)

# Open file from user input and read text file
data = open_and_read_file()
print(data)
