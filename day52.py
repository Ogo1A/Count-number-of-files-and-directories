import os

# Path in which we have to count files and directories
PATH = 'E:\\elements'  # Give your path here

fileCount = 0
dirCount = 0

for root, dirs, files in os.walk(PATH):
    print('Looking in:', root)
    for directories in dirs:
        dirCount += 1
    for Files in files:
        fileCount += 1

# Output the results
print('Number of files:', fileCount)
print('Number of directories:', dirCount)
print('Total:', dirCount + fileCount)
