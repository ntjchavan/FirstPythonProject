# This is especially useful for:
# Backup systems
# File organizers
# Moving uploaded files
# Creating application backups
# Cleaning temporary directories
# Log management

# shutil stands for shell utilities.
# It provides high-level operations for working with files and directories.

# Why Do We Need shutil
# os.remove()
# os.rename()
# os.mkdir()

# copytree() means:
# Copy a directory and everything inside it recursively.


import shutil

shutil.copy("files/data.txt", "files/backup/") # you can mention destination any file name as well
print("Backup Completed!")

# Important points
# shutil.copy()
#         ↓
# Copy a file

# shutil.copy2()
#         ↓
# Copy file + more metadata

# shutil.copytree()
#         ↓
# Copy directory recursively

# shutil.move()
#         ↓
# Move file/directory

# shutil.rmtree()
#         ↓
# Delete directory recursively

# shutil.disk_usage()
#         ↓
# Disk space information
