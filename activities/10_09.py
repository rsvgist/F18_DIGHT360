input('try ... except blocks\n\n')

# Errors halt a script. If you know that something you are doing could throw an
# error, there are two approaches:

# Look-before-you-leap
for i in range(3):
    if i == 0:
        print("You can't divide by zero!")
    else:
        print(1 / i)

# Better to ask forgiveness
for i in range(3):
    try:
        print(1 / i)
    except ZeroDivisionError:  # ...or just `except:`, but that is sloppy!
        print("You can't divide by zero!")
print()

# try ... except blocks are almost always faster and easier to read

###############################################################################

input('intro to nltk (http://www.nltk.org/book/)\n\n')

import nltk
# nltk.download('punkt')

print('### Tokenizing and `Text` objects')
raw_text = ('I\'ll bet you wish that you had come up with this sentence.'
            'Call me Dr. Brillant! Sir Robin\'s sentence was much worse.')
print(raw_text)
sents = nltk.sent_tokenize(raw_text)
print(sents)
tokens = nltk.word_tokenize(raw_text)
print(tokens)
my_text = nltk.Text(tokens)
print(dir(my_text))
print()

###############################################################################

input('### Download useful texts/corpora used in the nltk book\n\n')
print('''
>>> import nltk
>>> nltk.download('book')
''')

# Using * in import statements is TERRIBLE idiom, but we will do it this
# way because that is how they wrote the examples in the NLTK book.
# It is better to do `from nltk import book`, then refer to `book.text1`.
from nltk.book import *  

print('Text.concordance()')
print('Concordance of "monstrous" in Moby Dick:')
print(text1.concordance('monstrous'))
print()

print('Text.similar()')
print('Words in Moby Dick with contexts similar to "monstrous"')
print(text1.similar('monstrous'))
print('Words in Sense & Sensibility with contexts similar to "monstrous"')
print(text2.similar('monstrous'))
print()

print('How many tokens are in Genesis?')
print(len(text3))
print()

print('How many unique tokens ("types") are in Genesis?')
print('first 25:', sorted(set(text3))[:25])
print(len(set(text3)))
print()

print('What is the type-token ratio of Genesis?')
print(len(set(text3)) / len(text3))  # types / tokens
print()

print('What ratio of the words in Genesis are "smote"?')
print(text3.count('smote') / len(text3))
print()

print('PRACTICE A')
print('Write a script that imports all of the texts from nltk.book and then '
      'print a tab-separated table showing the type-token ratio of each text.')
print('\t* NOTE: Text objects have a `name` attribute: text1.name')
print()
input()

print('PRACTICE B')
print('Extend your script from PRACTICE A to also print the proportion of '
      'words that are articles: `a`, `an` and `the`.')
print('\t* NOTE: A regular expression is a good way to find articles.')
print()
input()

print('PRACTICE C')
print('Extend your script to also print other interesting features. '
      'Be creative.')
print()
input()

###############################################################################
print('BE LAZY!')
'''A special kind of laziness is very beneficial to programmers.
    * Clumsy code is very hard to write and maintain
    * Think like the person who is going to use your code.
    * What would be the easiest way to get this functionality?
    * Write the last line of code first, then write the code to make it work

In the PRACTICE exercises above, you might want to be able to write something
like this to print your tab-separated table:
print('Text', 'TTR', 'artTR', 'smoteTR', sep='\t')
for t in [text1, text2, text3, text4, text5, text6, text7, text8, text9]:
    print(t.name, ttr(t), artTR(t), smoteTR(t), sep='\t')

This is easy to read and easy to maintain. Now you just have to write functions
that will make it work.
    func_name   input   output
    ttr         Text    type-token ratio (float)
    artTR       Text    article-token ratio (float)
    smoteTR     Text    smote-token ratio (float)
    ...         ...     ...
'''
print('PRACTICE D')
print('Rewrite your code from PRACTICE A-C using functions as shown in the '
      'comment above.')
print()
input()

###############################################################################
print('Frequency distributions')

from nltk.probability import FreqDist

print('FreqDist of Batman theme song')
batman_fd = FreqDist(nltk.word_tokenize('na na na na na na na na na na na na na na na na Bat Man!'))
print(batman_fd.most_common(5))
print()
input()

print('How about words that only occur once? ("singletons" or "hapaxes")')
print(batman_fd.hapaxes())
print()
input()

print('What are the 50 most common words in Genesis?')
fd3 = FreqDist(text3)
print(fd3.most_common(50))
print()
input()

print('How frequent is "prayed" in Genesis?')
# FreqDist objects are sub-types of dict
print(fd3['prayed'])
print()

