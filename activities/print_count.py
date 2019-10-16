import sys

#print(sys.argv)

filenames = sys.argv[1:] # ignore 1st one in array : sys.argv

for fname in filenames:
    with open(fname) as f:
        contents = f.read()
    print(fname, contents.count('print('), sep = '\t')





