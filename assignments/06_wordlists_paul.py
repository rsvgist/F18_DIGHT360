# import libs
from glob import glob
from nltk.corpus import stopwords
from nltk import word_tokenize
import re

# stopwords as set()
stopword_set = set(stopwords.words('english'))
corpus = set()
words = {}
freqs = {}
corpus_files = glob('./Mini-CORE/*.txt')
for fname in corpus_files:
    # parse char placement in fname, grab the id
    subcorp = fname[14:16]
    if subcorp not in corpus:
        corpus.add(subcorp)
        words[subcorp] = set()
        freqs[subcorp] = {}
    with open(fname, 'r') as f:
        raw_txt = f.read()
    txt = re.findall(r'<(?:h|p)>(.*)', raw_txt)
    for line in text:
        tokens = word_tokenize(line)
        # count word tokens, add to total freq 
        for token in tokens:
            if token.lower() in stopword_set:
                continue
            if not token.lower() in words[subcorp]:
                words[subcorp].add(token.lower())
                freqs[subcorp][token.lower()] = 0
            freqs[subcorp][token.lower()] += 1

 # write freq data to files           
for subcorp in corpus:
    with open(subcorp + '-freqs.tsv', 'w') as data_file:
        data = sorted(freqs[subcorp].items(),
                      key=lambda x: x[1],
                      reverse=True)
        for word, freq in data:
            print(word, freq, sep='\t', file=data_file)
