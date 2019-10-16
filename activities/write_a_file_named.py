import sys

print(sys.argv)

filename = sys.argv[1]
print('fname: ', filename)
with open(filename, 'w') as my_file: 
    print('It worked!', file=my_file)




