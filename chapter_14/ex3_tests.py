# this file is for trying out things that might be
# useful in ch14 ex3
import os

paths = []
for root, dirs, files in os.walk('.'):
    for file_name in files:
        paths.append(os.path.join(root, file_name))


checksum_dict = {}
for path in paths:
    if path[-4:] == '.txt':
        cmd = 'md5 ' + path
        fp = os.popen(cmd)
        checksum = fp.read()

        checksum = checksum[-32:-3]

        if checksum in checksum_dict:
            checksum_dict[checksum].append(path)
        else:
            checksum_dict[checksum] = [path]

for value in checksum_dict.values():
    if len(value) > 1:
        print(value, "are likely duplicate files")
