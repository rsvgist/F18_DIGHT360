"""Demo sys.argv()."""

import sys

'''Call this script with arguments. For example, the following command...

$ python3 argv.py this is a test this is only a test

...prints out...

['argv.py', 'this', 'is', 'a', 'test', 'this', 'is', 'only', 'a', 'test']'''

print('sys.argv is...', sys.argv, type(sys.argv), sep='\n')
