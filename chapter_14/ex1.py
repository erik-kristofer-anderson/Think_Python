""" from think python chapter 14
Write a function called sed that takes as arguments a pattern
string, a replacement string, and two filenames;
it should read the first file and write the contents
into the second file (creating it if neccessary). If
the pattern string appears in anywhere in the file,
kt should be replaced with the replacement string.
"""

def sed(pattern, replacement, filename1, filename2):
    # open filename1
    fin = open(filename1)

    # read its contents to a string
    s = fin.read()

    # replace all cases of pattern in this string with
    # replacement
    s = s.replace(pattern, replacement)

    # write the result to filename2
    fout = open(filename2, 'w')
    fout.write(s)
    fout.close()

pattern = 'asdf'
replacement = 'whales'
filename1 = 'test_text.txt'
filename2 = 'test_output.txt'
sed(pattern, replacement, filename1, filename2)
