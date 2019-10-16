import spacy
from spacy import displacy

nlp = spacy.load('en')

doc = nlp("Next week I'll be in Madrid.")
print([(token.text, token.tag_) for token in doc])
 
# [('Next', 'JJ'), ('week', 'NN'), ('I', 'PRP'), ("'ll", 'MD'), ('be', 'VB'), ('in', 'IN'), ('Madrid', 'NNP'), ('.', '.')]
 
print('Find named entities, phrases and concepts...')
doc = nlp('Apple is looking at buying U.K. startup for $1 billion, which is a gid deal in America to Trump.')


#matplotlib? np???

#np idea
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

print(*'token, start, end, label'.split(), sep='\t')
ent_list = []
for ent in doc.ents:
    x = ent.label_
    ent_list.append(x)
     
    print(ent.text, ent.start_char, ent.end_char, ent.label_, sep='\t')
print('Make named entity visualization on localhost...')
ent_freqs = Counter(ent_list)
df = pd.DataFrame.from_dict(ent_freqs, orient='index')
df.plot(kind='bar')
plt.show()

displacy.serve(doc, style='ent')

"""
import random
import requests as r
import time

comics_responses = []
google = 'https://www.google.com/search?q='
for term in ['xkcd', 'smbc', 'calvin+and+hobbes']:
    comics_responses.append(r.get(google + term, headers=headers))
    time.sleep(random.uniform(1.5, 2.5))  # Let the server breathe
for each_response in comics_responses:
    print('Do stuff with those websites here...')





#from some gh thing
import urllib.request as urllib2
from bs4 import BeautifulSoup
import pandas as pd
import re
from unidecode import unidecode

quote_page = 'http://metrolyrics.com/{}-lyrics-drake.html'
filename = 'mj-songs.csv'
songs = pd.read_csv(filename, encoding= "utf-8")

for index, row in songs.iterrows():
    page = urllib2.urlopen(quote_page.format(row['song']))
    soup = BeautifulSoup(page, 'html.parser')
    verses = soup.find_all('p', attrs={'class': 'verse'})

    lyrics = ''

    for verse in verses:
        text = verse.text.strip()
        text = re.sub(r"\[.*\]\n", "", unidecode(text))
        if lyrics == '':
            lyrics = lyrics + text.replace('\n', '|-|')
        else:
            lyrics = lyrics + '|-|' + text.replace('\n', '|-|')

    songs.at[index, 'lyrics'] = lyrics

    print('saving {}'.format(row['song']))
    songs.head()

print('writing to .csv')
songs.to_csv(filename, sep=',', encoding='utf-8')
"""