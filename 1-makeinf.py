import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

"""
This program creates folders by reading input from a text file.
Each line in the file creates one folder.
"""

# Create the Tkinter app
root = tk.Tk()
root.withdraw()

# Show the first info box
messagebox.showinfo(
            "Folder creation tool",
            "Welcome, please provide a file containing the folder names and an output folder." 
        )

# Get the file and folder path
open_file_path = filedialog.askopenfilename(parent=root,initialdir="/",title='Please select a file to read the folder names from')

if not open_file_path:
    quit()

dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory where the folders are created')

if not dirname:
    quit()
    
# Error handling variables    
file_error_list = []
error_occurred = False

try:
    # Open file
    with open(open_file_path, 'rU') as x:
        # Loop through each line
        for line in x:
            # Remove possible whitespace characters in beginning and end with strip()
            # split the string into a list with split()
            line = line.strip().split()
            # Concatenate the list items
            filename = " ".join([i for i in line])
            # create the full directory path
            full_path = dirname + "/" + filename
            try:
                # Create the new directory
                os.mkdir(full_path)
            except (FileNotFoundError, IOError):
                file_error_list.append(filename)
                error_occurred = True
                
except (FileNotFoundError, IOError):
    messagebox.showwarning(
            "Something went wrong, exiting",
            "Tried to create folders here: {}".format(dirname)     
    )
    
if not error_occurred:    
    messagebox.showinfo(
        "Folders created",
        "You can find your folders here: {}".format(dirname) 
        )

else:
    file_error_string = ""
    for file_name in file_error_list:
        file_error_string += file_name
        file_error_string += "\n"   
    messagebox.showwarning(
        "Error creating folders",
        "Tried to create folders here: {}".format(dirname) + "\n"\
        "Following folders could not be created:\n" +
        file_error_string
        )        