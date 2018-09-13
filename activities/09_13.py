"""In-class activities for 09-19."""

# standard library and namespace manipulation
# regular expressions
# precision and recall

# warm-up
"""6) Write a program that asks the user for a word of at least six letters in
length, then prints back to the user on one line the first three letters, and
then on a second line prints the last three letters.

7) Modify the program to print out every other letter.

8) Modify the program to print out the word spelled backward."""

###############################################################################
# standard library

# python comes with lots of useful tools available in the "standard library".
# https://docs.python.org/3/library/index.html
# Some very commonly used modules include...
#     re - regular expressions
#     datetime - basic date and time types
#     collections - useful variations on dicts, for example
#     pprint - print objects prettily (with readable indentations)
#     math
#     random - random number generation and random sampling
#     statistics
#     os - interact with operating system (filesystem)
#     pickle - object serialization
#     csv - read/write csv data files
#     html - HTML
#     urllib - URL handling modules (e.g., for web scraping)


###############################################################################
print('importing modules')
print('=' * 79)
# `import`, `from`, and `as`

# The "namespace" is all of the names that have been assigned
# In other words, it is everything that is available to be used

# You can get a standard library module into the namespace by `import`ing it:
import re
print('This is the contents of the `re` module:\n', dir(re))
print()

# You can also just import part of a module using `from`
print('Let\'s try some math!')
from math import log
from math import e

print('What is the meaning of life, the universe, and everything?',
      log(e ** 42))  # 42
print('The value of e is', e)
print()

# As you import something, you can assign it a custom name using `as`
print('Let\'s alias something as we import it!')
print('importing e...')
from math import e
print('importing e as wahoo...')
from math import e as wahoo
print('T/F: e and wahoo are equal:', e == wahoo)
print()

# To summarize, the following three approaches all achieve the exact same thing

print('approach 1')
import statistics
avg = statistics.mean
print('The average of [1,2,3] is:', avg([1, 2, 3]))
# or...
# print('The average of [1,2,3] is:', statistics.mean([1, 2, 3]))
print()

print('approach 2')
from statistics import mean
avg = mean
print('The average of [1,2,3] is:', avg([1, 2, 3]))
# or...
# print('The average of [1,2,3] is:', mean([1, 2, 3]))
print()

print('approach 3')
from statistics import mean as avg
print('The average of [1,2,3] is:', avg([1, 2, 3]))
print()
print()

###############################################################################
print('Regular expressions')
print('=' * 79)

# Python has an excellent regular expression module in the standard library

# Quotation from python documents:

# Regular expressions use the backslash character ('\') to indicate special
# forms or to allow special characters to be used without invoking their
# special meaning. This collides with Python’s usage of the same character for
# the same purpose in string literals; for example, for a regular expression to
# match a literal backslash, one might have to write '\\\\' as the pattern
# string, because the regular expression must be \\, and each backslash must be
# expressed as \\ inside a regular Python string literal.  To sidestep
# "backslash hell" use Python’s raw string notation for regular expression
# patterns: backslashes are not handled in any special way in a string literal
# prefixed with 'r'.... Usually patterns will be expressed in Python code using
# this raw string notation. The python interpreter treats r'/t' and '\\t' as
# equivalent expressions.

import re
test_str = 'I would like spam, ham, and eggs.'
test_re = r'spam|ham|eggs'
print('test string:', test_str)
print('test regex:', test_re)
# re.search() only finds the first match
result = re.search(test_re, test_str)
print('re.search():', result)

# re.findall() finds all matches, returns list
result2 = re.findall(test_re, test_str)
print('re.findall():', result2)

# re.finditer() finds all matches, returns list-like iterator of Match objects
result3 = re.finditer(test_re, test_str)
print('re.finditer():')
for i in result3:
    print('\t', i)

# re.match() only finds a match at the beginning of the string
result4 = re.match(test_re, test_str)
print('re.match():', result4)

# re.sub() substitutes a string for every match
result5 = re.sub(test_re, 'spam', test_str)
print('re.sub():', result5)

# re.sub() can refer back to groups that you create using parentheses
result6 = re.sub(r'(spam)|(ham)|(eggs)', r'\1\3spam\2\3', test_str)
print('re.sub(): (groups):', result6)
print()
print()

###############################################################################
# precision and recall

# When you report accuracy at classifying something, precision and recall are
# commonly-used metrics.
# https://en.wikipedia.org/wiki/Precision_and_recall
# tp = True Positive
# tn = True Negative
# fp = False Positive
# fn = False Negative

# Precision = tp / (tp + fp)  # of all the positives, how many were correct?
# Recall = tp / (tp + fn)  # of all the trues, how many were identified?

###############################################################################
# list comprehensions

print(list(range(5)))
print([i * 10 for i in range(5)])
print([i * 10 for i in range(5) if i > 2])
