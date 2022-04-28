import os

# This gives us the absolute(full) path to this python script
file_path = os.path.abspath(__file__)

# Do stuff -- I just created a folder
os.system("mkdir %USERPROFILE%\Desktop\dontlook")

# At the end of the script, the file is deleted & over-written
os.remove(file_path)
folder_path = os.path.dirname(file_path)
os.system("cipher /W:%s" % folder_path)

#The Python codes needed to actually delete a file/folder are given in [this](https://stackoverflow.com/questions/6996603/how-do-i-delete-a-file-or-folder-in-python) stackoverflow accepted answer, those being:

# os.remove       - will remove a file.
# os.rmdir()      - will remove an empty directory.
# shutil.rmtree() - will delete a directory and all its contents.

# As you may have guessed, this doesn't overwrite the deleted data like 'shred' does on Linux. However, there is a Windows command 'cipher' whose particulars you can see for yourself (either by looking here: https://support.microsoft.com/en-us/kb/315672, or typing 'cipher /?' into a CMD prompt. The following windows command will overwrite deleted data on the specified volume and/or directory:

# 'cipher /w:drive_letter:\folder_name'

# My own tests on Windows 7 successfully delete the script and appear to overwrite the data... however, since I haven't attempted to retrieve the deleted script forensically, I can't yet vouch for that 100%. But the Windows docs for 'cipher' above do seem confident with themselves.

# Something to maybe bear in mind.. possible very lengthy overwrite times with 'cipher' depending on the size of the target folder/drive. Test this out first.

