"""Create topic model from given year and month of general conference.

USAGE: $ python3 grab_conference.py 2017-10 10 10
                                    YEAR-MO
                                            ^^ = # of topics
                                               ^^ = # of words
"""
import csv
# import html
import os
import random
import re
import requests
import string
import sys
from time import sleep

from bs4 import BeautifulSoup
import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

# import nltk
# nltk.download('stopwords'):


def get_url(url):
    """Spoof user agent and get html."""
    sleep(random.uniform(0.5, 1.5))
    h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/35.0.1916.47 Safari/537.36'}
    return requests.get(url, headers=h).text


conference = sys.argv[-3].split('-')
year = conference[0]
month = conference[1]


def file2str(filename):
    try:
        with open(filename) as file:
            string = file.read()
            return string
    except FileNotFoundError:
        print(f'{filename} was not found.')
        return False


def str2file(string, filename):
    try:
        with open(filename, 'wt') as file:
            file.write(string)
    except:
        print(f'Could not write to {filename}.')


def dir2dict(path):
    if path[-1:] != '/':
        path += '/'
    if path[0:2] != './':
        path = './' + path
    files = {}
    try:
        for file in os.listdir(path):
            if file[0:1] != '.':  # Skip hidden files like .DS_Store
                files[file] = file2str(path + file)
    except:
        print(f'Could not open {path}.')
    return files


# Download Index

url = f'https://www.lds.org/general-conference/{year}/{month}?lang=eng'

# Check data dir
if not os.path.isdir('indexes'):
    os.mkdir('indexes')

# Download Talks

if not os.path.isdir('gc_html'):
    os.mkdir('gc_html')

# Should only download if file does not exist.
index_filename = f'indexes/index_{year}_{month}.html'
if not os.path.isfile(index_filename):
    print('Getting index...')
    index_html = get_url(url)
    str2file(index_html, index_filename)
else:
    print('Opening index from', index_filename, '...')
    index_html = file2str(index_filename)

urls = re.findall(f'a href="/general-conference/{year}/{month}/([^?]+)?', index_html)
urls = [f'https://www.lds.org/general-conference/{year}/{month}/{x}' for x in urls]

for url in urls:
    talk_title = url.split('/')[-1]
    output_file = f'gc_html/{year}-{month}_{talk_title}.html'
    if os.path.isfile(output_file) is False:
        print(f'Downloading {url}...')
        the_html = get_url(url)
        str2file(the_html, output_file)
    else:
        print('Skipping {url}...')

# Clean talks in to a list

talk_files = dir2dict('gc_html')
# Only take the talks from this conference
talks = {x: y for x, y in talk_files.items() if f'{year}-{month}_' in x}

# Nodes table
output_file = f'nodes_{year}_{month}.csv'
if os.path.isfile(output_file):
    print('Skipping nodes table.')
else:
    rows = []
    rows.append('Id,Label,Conference,Title,Speaker,Position'.split(','))

    for talk, talk_html in talks.items():
        print('Processing ' + talk)
        soup = BeautifulSoup(talk_html, 'html.parser')
        row = []
        row.append(talk)  # id
        row.append(talk)  # label
        row.append(f'{year}-{month}')  # conference
        row.append(soup.findAll('h1', {'class': 'title'})[0].get_text())  # title

        speaker = soup.findAll('a', {'class': 'article-author__name'})
        if len(speaker) > 0:
            speaker = speaker[0]
            speaker = speaker.get_text()
        else:
            speaker = ''

        # Only way to get the &nbsp; to render properly.
        # speaker = speaker.replace('\xa0', ' ')
        speaker = speaker.encode('utf-8', 'surrogateescape').decode('utf-8', 'replace')
        if speaker.lower()[0:3] == 'by ':
            speaker = speaker[3:]
        row.append(speaker)  # speaker
        row.append(soup.findAll('p', {'class': 'article-author__title'})[0].get_text())  # position
        rows.append(row)

    with open(output_file, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in rows:
            csv_writer.writerow(row)

# Topic Model

if os.path.isdir('gc_texts') is False:
    os.mkdir('gc_texts')

# Get texts
ids = []
print('Compiling texts')
doc_complete = []
titles = []
for talk, talk_html in talks.items():
    ids.append(talk)
    titles.append(talk)
    soup = BeautifulSoup(talk_html, 'html.parser')
    text = soup.findAll('div', {'class': 'article-content'})[0].get_text(separator=' ')
    text = text.encode('utf-8', 'surrogateescape').decode('utf-8', 'replace')

    str2file(text, f'gc_texts/{talk}')
    doc_complete.append(text)

# doc_complete = ['the quick test', 'the slow trial', 'a trial by jury']

print('Starting LDA')
topic_count = int(sys.argv[-2])
word_count = int(sys.argv[-1])
# https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()


def clean(doc):
    stop_free = ' '.join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = ' '.join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


doc_clean = [clean(doc).split() for doc in doc_complete]

# Creating the term dictionary of our corpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Training LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=topic_count, id2word=dictionary, passes=50)

topic_keys = ldamodel.print_topics(num_topics=topic_count, num_words=word_count)
print('topic_keys:\n', topic_keys)
rows = []
for key in topic_keys:
    topic = key[0]
    loadings = key[1]
    # loadings = [x.strip for x in str(loadings).split('+')]
    y = loadings.split('+')
    y = [x.split('*')[1].replace('"', '').strip() for x in y]
    rows.append([topic] + y)
with open('topic_keys.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in rows:
        csv_writer.writerow(row)

# Output document loadings
rows = []
rows.append('Source,Target,Type,Weight'.split(','))
for i in range(0, len(doc_term_matrix)):
    doc_topics = ldamodel.get_document_topics(doc_term_matrix[i])
    for topic in doc_topics:
        row = [ids[i], topic[0], 'Undirected', topic[1]]
        rows.append(row)
with open('doc_topics.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in rows:
        csv_writer.writerow(row)


"""Example of visualizing topic model using ForceAtlas2 algorithm."""

from fa2 import ForceAtlas2  # pip install fa2
import matplotlib.pyplot as plt
import networkx as nx

with open('doc_topics.csv') as t_file:
    e = t_file.readlines()[1:]  # first line is header
edges = []
for line in e:
    line = line.split(',')
    edges.append((line[0][8:-5], line[1], line[3]))


g = nx.Graph()
g.add_weighted_edges_from(edges)
print(g.edges())

forceatlas2 = ForceAtlas2(# Behavior alternatives  # noqa: E261
                          outboundAttractionDistribution=False,  # Dissuade hubs
                          linLogMode=False,  # NOT IMPLEMENTED
                          adjustSizes=False,  # Prevent overlap (NOT IMPLEMENTED)
                          edgeWeightInfluence=1.0,

                          # Performance
                          jitterTolerance=1.0,  # Tolerance
                          barnesHutOptimize=True,
                          barnesHutTheta=1.2,
                          multiThreaded=False,  # NOT IMPLEMENTED

                          # Tuning
                          scalingRatio=2.0,
                          strongGravityMode=False,
                          gravity=4.0,

                          # Log
                          verbose=True)

positions = forceatlas2.forceatlas2_networkx_layout(g, pos=None, iterations=2000)
print(positions)
nx.draw_networkx(g, positions, cmap=plt.get_cmap('jet'), node_size=75,
                 with_labels=True, font_size=6,
                 label=f'Topics in {month}-{year} General Conference')
plt.show()
