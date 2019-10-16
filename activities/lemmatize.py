import nltk
# assert nltk.download('wordnet')
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

print('Building stemmer and lemmatizer...')
stemmer = SnowballStemmer('english')  # also available: danish dutch english finnish french german hungarian italian norwegian porter portuguese romanian russian spanish swedish
lemmatizer = WordNetLemmatizer()
input('[enter] to continue\n')

words = 'cat cats goose geese identified nonsensical pluralistic rock rocks leaves fairly grows'.split()
words1 = 'The abolitionists reformulated their counterarguments against the proposed legislation.'.split()

print('Normalizing some `words`...')
print('{:<20}{:<20}{:<20}'.format('WORD', 'STEM', 'LEMMA'))
for w in words1:
    print('{:<20}{:<20}{:<20}'.format(w, stemmer.stem(w), lemmatizer.lemmatize(w)))



def pos_lemmatize(string):
    toks = nltk.word_tokenize(string)
    tagged = nltk.pos_tag(toks) # this returns a tuple: (token, tag)
    output = []
    for tok, tag in tagged:
        if tag[0] == 'J':
            output.append(lemmatizer.lemmatize(tok, 'a'))
        elif tag[0] == 'V':
            output.append(lemmatizer.lemmatize(tok, 'v'))
        else:
            output.append(lemmatizer.lemmatize(tok))
    return output
        
print(pos_lemmatize('This isn\'t the first the first example, but it might be the last!'))

