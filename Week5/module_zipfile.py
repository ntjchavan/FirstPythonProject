# pathlib → paths
# os → operating-system operations
# shutil → copy/move/delete files and directories

# Zipfile : This is especially useful for:

# Creating backups
# Compressing files
# Extracting files
# Archiving logs
# Packaging reports
# Sending multiple files as one archive

# Python provides the zipfile module for working with .zip files.

import zipfile

with zipfile.ZipFile(
    "backup.zip", "w"
) as zip_file:

    zip_file.write(
        "files\data.txt"
    )

# add multiple files
with zipfile.ZipFile(
    "backup.zip",
    "w",
    compression=zipfile.ZIP_DEFLATED
) as zip_file:

    zip_file.write("files\employees.csv")
    zip_file.write("files\students.csv")
    zip_file.write("files\data.txt")