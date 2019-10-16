"""In-class activities for 11-27."""


print('''Lemmatizing and stemming

Stem: an abstraction that groups multiple words together
Lemma: the headword you can look up in the dictionary

Stemmer: converts a word to its stem
Lemmatizer: converts a word to its lemma
''')

import nltk
assert nltk.download('wordnet')
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

print('Building stemmer and lemmatizer...')
stemmer = SnowballStemmer('english')  # also available: danish dutch english finnish french german hungarian italian norwegian porter portuguese romanian russian spanish swedish
lemmatizer = WordNetLemmatizer()
input('[enter] to continue\n')

words = 'cat cats goose geese identified nonsensical pluralistic rock rocks leaves fairly grows'.split()


print('Normalizing some `words`...')
print('{:<14}{:<12}{:<12}'.format('WORD', 'STEM', 'LEMMA'))
for w in words:
    print('{:<14}{:<12}{:<12}'.format(w, stemmer.stem(w), lemmatizer.lemmatize(w)))

input('Press [return] to continue.\n')


print('''PRACTICE A

Open a new file and write a python script that stems and lemmatizes the
following sentence:

The abolitionists reformulated their counterarguments against the proposed legislation.

''')
input('Press [return] to continue.\n')


print('''WordNetLemmatizer assumes that everything you give it is a noun. Very
often, this is a bad assumption. A different part of speech can be specified
using the `pos` keyword argument.''')

print('better A', stemmer.stem('better'), lemmatizer.lemmatize('better', pos='a'), sep='\t')
print('better N', stemmer.stem('better'), lemmatizer.lemmatize('better', pos='n'), sep='\t')
print('better V', stemmer.stem('better'), lemmatizer.lemmatize('better', pos='v'), sep='\t')
print('running A', stemmer.stem('running'), lemmatizer.lemmatize('running', pos='a'), sep='\t')
print('running N', stemmer.stem('running'), lemmatizer.lemmatize('running', pos='n'), sep='\t')
print('running V', stemmer.stem('running'), lemmatizer.lemmatize('running', pos='v'), sep='\t')
input('Press [return] to continue.\n')


print('''PRACTICE B

Write a function called `pos_lemmatize` that uses nltk.pos_tag() to determine
which part of speech the lemmatizer should use. The function should take a
tokenized text as input (list of strings) and return a corresponding lemmatized
text (list of strings).

''')

input('Press [return] to continue.\n')

print('''FINAL PROJECT PRESENTATIONS

Thur 13 Dec 2018 3-6pm in B013 JFSB

Each student will have 5-10 mins to present their final project.
Your presentation should include...
    * Introduction (motivation for the project)
    * Methods
        - How you obtained your corpus
        - How you preprocessed your corpus
        - How you extracted the data you needed
    * At least one data visualization (boxplot, scatterplot, histogram, etc.)
    * Results and conclusions
    * Be prepared to answer questions from the audience after your presentation

The presentation itself accounts for 20% of the grade for the final project.

The remaining 80% of the final project is simply your code. Make sure that it
is easy to read, following PEP8 standards, with comments explaining parts that
are not self-explanatory. If you would like to explain anything about your
approach, you may also submit a separate explanation, but it must fit on one
double-spaced page with 12-pt font.
''')
input('Press [return] to continue.\n')

from nltk.tree import Tree
from nltk.draw.tree import TreeView

print('''Syntactic parsing

Syntax refers to the way that words are arranged in a sentence, and the
grammatical relations between words.

Compare the following sets of sentences:

UNGRAMMATICAL: (word soup; no cohesive relation between words)
He roared with me the pail slip down his back.
The worst part and clumsy looking for whoever heard light.

GRAMMATICAL: (cohesive relation between words)
The book's ending was the worst part and the best part for me.
On land they are slow and clumsy looking.
Colorless green ideas sleep furiously. (meaningless, but grammatical.)

A syntactic parser is simply a tool that tries to annotate the relations
between words. There are MANY different kinds of parsing algorithms, and even
more theories of syntax describing the kinds of annotations that can be made.
Today we will see a couple simple examples.
''')

input('Press [return] to continue.\n')

print('#' * 79)
print('''Dependency parsing

Dependency parsing is arguably the most atheoretic approach to syntax. It does
not assume any hidden grammatical apparatus. It just draws connections between
words and (optionally) labels what kind of relation holds between those words.

The state-of-the-art dependency parser is called `maltparser`, and nltk
includes an interface to `maltparser`, but maltparser must be installed
separately. (For the sake of time we won't be using it, but you can google it.)

''')

input('Look at the following code for dependency parsing.\n')

toy_dep_grammar = nltk.DependencyGrammar.fromstring("""
    'shot' -> 'I' | 'elephant' | 'in'
    'elephant' -> 'an' | 'in'
    'in' -> 'pajamas'
    'pajamas' -> 'my'
    """)
pdp = nltk.ProjectiveDependencyParser(toy_dep_grammar)
sent = 'I shot an elephant in my pajamas'.split()
print(f'parsing {sent.__repr__}...')
ptrees = pdp.parse(sent)
for i, tree in enumerate(ptrees):
    print(tree, tree.height())
    TreeView(tree)._cframe.print_to_file(f'dep_tree{i}.ps')

print('to convert images, run...\n $ convert tree0.ps tree0.png')

input('[enter] to continue.\n')

print('\n' + '#' * 79)
print('''Constituency parsing

Some theories of syntax assume that there are implicit structures to annotate,
such as Noun Phrases (NP), Verb Phrases (VP), etc.
''')

# CFG = Context-Free Grammar
toy_cfg_grammar = nltk.CFG.fromstring("""
    S -> NP VP
    PP -> P NP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    Det -> 'an' | 'my'
    N -> 'elephant' | 'pajamas'
    V -> 'shot'
    P -> 'in'
    """)
chart_parser = nltk.ChartParser(toy_cfg_grammar)
for i, tree in enumerate(chart_parser.parse(sent)):
    print(tree, tree.height())
    TreeView(tree)._cframe.print_to_file(f'const_tree{i}.ps')

# The Tree object has lots of useful methods
print('tree.height():', tree.height())  # How "tall" (complex?) is the tree?
print('tree.leaves():', tree.leaves())  # List of only the surface words
print('tree.pos():', tree.pos())  # part-of-speech tagged sentence (flattened)
# tree.draw()  # Will only work in a gui environment

