import nltk

print('Named entity recognition')
print('Get random sentence from tagged treebank...')
sent = nltk.corpus.treebank.tagged_sents()[22]
print(' '.join([w for w, tag in sent]))
print('-' * 25)
print('Recognizing named entities...')
print(nltk.ne_chunk(sent, binary=True))  # `binary`= named entity or not?
input('Press [return] to continue')

print('-' * 25)
print('Recognizing named entities (with labels this time)...')
print(nltk.ne_chunk(sent))  # entity category labels added
input('Press [return] to continue')

###############################################################################
# Labels include:
# NE Type       Examples
# ORGANIZATION  Georgia-Pacific Corp., WHO
# PERSON        Eddy Bonte, President Obama
# LOCATION      Murray River, Mount Everest
# DATE          June, 2008-06-29
# TIME          two fifty a m, 1:30 p.m.
# MONEY         175 million Canadian Dollars, GBP 10.40
# PERCENT       twenty pct, 18.75 %
# FACILITY      Washington Monument, Stonehenge
# GPE           South East Asia, Midlothian
###############################################################################

