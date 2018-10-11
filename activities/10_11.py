"""In-class activities for 10-11.py"""

# globs

###############################################################################
print('Globs')

print('''Globs are a kind of simplified regular expression, usually used for
selecting files. Globs are especially common in bash commands like ls, cp, mv,
etc.

https://en.wikipedia.org/wiki/Glob_(programming)#Syntax
''')

print('''PRACTICE A
Open a bash shell and navigate to the DIGHT360_Fall2017/activities/ folder.
Use the `ls` command to select files that...:
    * ...end in `.py`
    * ...begin with a capital letter
    * ...have an s
    * ...end in `.txt`
    * ...begin with a 1
    * ...has exactly eight characters

''')

print('''PRACTICE B
Now open a python shell in that same directory (type `python3` in bash).
>>> from glob import glob
>>> glob('*.txt')
['jokes.txt']

Try the other patterns from PRACTICE A.

''')

print('''PRACTICE C
Write a python script that opens all the files in the current directory that
end with `.txt` and print each line that contains the letter 'r'.

''')
