# write a program that searches a directory and all of its subdirectories
# recursively, and returns a list of complete paths for all files with
# a given suffix (like .mp3).
# hint: os.path provides several useful functions for manipulating file and path
# names

# first task... read the contents of a directory
import os

cmd = 'ls'
fp = os.popen(cmd)
res = fp.read()

lines = res.split('\n')

# next task: get the checksum for each of these, and store to a list
checksums = []
for line in lines:

    if '.' in line:
        filename = line
        cmd = 'md5 ' + filename
        fp = os.popen(cmd)
        res = fp.read()
        checksums.append(res)


next task: identify duplicate checksums
duplicates = []
for checksum in checksums:
    for checksum2 in checksums:
        if checksum == checksum2:
            duplicates.append(checksum)


print(duplicates)
# this doesn't work right because ... checksum and checksum2 come from the same list so there
# will always be duplicats
# commit this and backup and rework it
