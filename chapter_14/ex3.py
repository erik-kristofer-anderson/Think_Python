# write a program that searches a directory and all of its subdirectories
# recursively, and returns a list of complete paths for all files with
# a given suffix (like .mp3).
# hint: os.path provides several useful functions for manipulating file and path
# names

# first task... read the contents of a directory
import os

def get_ls():
    cmd = 'ls'
    fp = os.popen(cmd)
    res = fp.read()
    lines = res.split('\n')
    return lines # TODO this breaks by splitting by spaces in
# file names. for now I will sanatize the filenames of spaces
# but later I'd like to generalize this to handle spaces

# next task: get the checksum for each of these
# and make a dict of checksum to file names
### TODO generalize this to relaatave or absolute path

def make_checksum_dict():
    lines = get_ls()
    checksum_dict = {}
    for line in lines:


        if '.' in line:

            filename = line
            cmd = 'md5 ' + filename
            fp = os.popen(cmd)
            checksum = fp.read()


            checksum = checksum[-32:-3]

            if checksum in checksum_dict:
                checksum_dict[checksum].append(filename)
            else:
                checksum_dict[checksum] = [filename]
        else: # if '.' not in line
            pass # search the stuff in that directory

    return checksum_dict





checksum_dict = make_checksum_dict()
#print(checksum_dict)
for item in checksum_dict.items():
    print(item)


# now: move code into functions
