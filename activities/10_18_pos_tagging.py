"""In-class activities for part-of-speech tagging."""

import nltk

# Make sure necessary data has been downloaded
# nltk.download() returns True if it is (already) successfully downloaded
assert nltk.download('averaged_perceptron_tagger')
assert nltk.download('averaged_perceptron_tagger_ru')
assert nltk.download('punkt')

print('Part-of-speech tagging in English...')
walking = 'Dan did the walking man while walking down the path for walking.'
walking_tokens = nltk.word_tokenize(walking)
walking_tagged = nltk.pos_tag(walking_tokens)
print(walking_tagged)
# nltk.help.upenn_tagset() # print tagset from the Penn Treebank
print('https://www.clips.uantwerpen.be/pages/mbsp-tags')
print()
input('[enter] to continue...')

print('Part-of-speech tagging in Russian...')
rus_sent = 'Они стали говорить о стали.'
rus_tokens = nltk.word_tokenize(rus_sent)
rus_tagged = nltk.pos_tag(rus_tokens, lang='rus')
print(rus_tagged)
print('http://ruscorpora.ru/corpora-morph.html')
print()
input('[enter] to continue...')

print('''PRACTICE A
Try to come up with sentences that 'break' the pos-tagger, i.e. get the tagger
to put the wrong tag on a word or words.
''')
print()
input('[enter] to continue...')


print('How to iterate over tagged text...')
print('Each token is a 2-tuple (token, tag). Unpacking is your friend.')
print('This example shows how to print all of the nouns in the text:')
for token, tag in walking_tagged:
    if tag.startswith('N'):
        print(token)
input('[enter] to continue...')


print('''PRACTICE B
Write a script that part-of-speech tags the following text (`vcs`). Then
compute the proportion of words that are...
    * verbs
    * nouns
    * articles
    * etc.

List comprehensions are encouraged for filtering your text! :-)
''')

vcs = '''A component of software configuration management, version control, also
known as revision control or source control, is the management of changes to
documents, computer programs, large web sites, and other collections of
information. Changes are usually identified by a number or letter code, termed
the "revision number", "revision level", or simply "revision". For example, an
initial set of files is "revision 1". When the first change is made, the
resulting set is "revision 2", and so on. Each revision is associated with a
timestamp and the person making the change. Revisions can be compared, restored,
and with some types of files, merged. The need for a logical way to organize and
control revisions has existed for almost as long as writing has existed, but
revision control became much more important, and complicated, when the era of
computing began. The numbering of book editions and of specification revisions
are examples that date back to the print-only era. Today, the most capable (as
well as complex) revision control systems are those used in software
development, where a team of people may change the same files. Version control
systems (VCS) most commonly run as stand-alone applications, but revision
control is also embedded in various types of software such as word processors
and spreadsheets, collaborative web docs and in various content management
systems, e.g., Wikipedia's Page history. Revision control allows for the ability
to revert a document to a previous revision, which is critical for allowing
editors to track each other's edits, correct mistakes, and defend against
vandalism and spamming. Software tools for version control are essential for the
organization of multi-developer projects.'''


