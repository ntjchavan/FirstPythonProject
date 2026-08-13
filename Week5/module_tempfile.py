# tempfile is a Python standard-library module used to create temporary:
# Files
# Directories
# File-like objects

# Temporary files are useful when your program needs a place to store data only for a short period of time.

# Common methods
# "r"   -> read
# "w"   -> write
# "r+"  -> read + write
# "w+"  -> write + read
# "a"   -> append
# "a+"  -> append + read

import tempfile

temp_file = tempfile.TemporaryFile()

temp_file.write(
    b"Hello Python"
) # b means bytes

temp_file.seek(0)

print(
    temp_file.read()
) # b'Hello Python'

temp_file.close()


print("\n----------- With function ----------")
with tempfile.TemporaryFile() as temp_file:

    temp_file.write(
        b"Temporary file data"
    )

    temp_file.seek(0)

    print(temp_file.read()) # b'Temporary file data'

