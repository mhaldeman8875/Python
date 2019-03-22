#For this drill, you will need to write a script that will check a 
#specific folder on the hard drive, verify whether those files end 
#with a “.txt” file extension and if they do, print those qualifying 
#file names and their corresponding modified time-stamps to the console.

    #Your script will need to use the listdir() method from the OS module to iterate through all files within a specific directory.
    #Your script will need to use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute path.
    #Your script will need to use the getmtime() method from the OS module to find the latest date that each text file has been created or modified.
    #Your script will need to print each file ending with a “.txt” file extension and its corresponding mtime to the console.

import os

fpath = "C:\\Users\\madel\\Desktop\\Python\\Drill2Files"

for obj in os.listdir(fpath):
    mtime = os.path.getmtime(fpath)
    if obj.endswith(".txt"):
        print(os.path.join(fpath, obj), "Last Modified: ", mtime)