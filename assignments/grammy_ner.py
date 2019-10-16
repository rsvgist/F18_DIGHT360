"""In-class activities for 12-06."""

# Install: python3 -m pip install spacy && python3 -m spacy download en

print('importing spacy...')
import spacy
from spacy import displacy

print('Load English tokenizer, tagger, parser, NER and word vectors...')
nlp = spacy.load('en')
print('nlp:', type(nlp), dir(nlp))


MC_DIR_gd = 'D:\\python_projects\\F18_DIGHT360\\assignments\\final_grammynoms_61_clean.txt'
MC_DIR_bb = 'D:\\python_projects\\F18_DIGHT360\\assignments\\final_grammy_noms_clean.txt'
print('Process a document...')
with open(MC_DIR_bb, encoding='utf-8') as f:
    grammy = f.read()
doc_bb = nlp(grammy)
print('doc_bb:', type(doc_bb), dir(doc_bb))

print('Process a document...')
with open(MC_DIR_gd, encoding='utf-8') as f:
    grammy = f.read()
doc_gd = nlp(grammy)
print('doc_gd:', type(doc_gd), dir(doc_gd))

# print(*'token lemma POS tag dep shape alpha stop'.split(), sep='\t')
# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#           token.shape_, token.is_alpha, token.is_stop, sep='\t')
# print('explain what the JJ tag means:', spacy.explain('JJ'))

# print('Make dependency visualization of the document on localhost...')
# displacy.serve(doc, style='dep')

# print('...or just save it as a file...')
# svg = displacy.render(doc, style='dep')
# with open('dep_ex.svg', 'w', encoding='utf-8') as f:
#     f.write(svg)

print('Find named entities, phrases and concepts...')
#doc = nlp('Apple is looking at buying U.K. startup for $1 billion')




#np idea, change doc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter



"""
#make a plot too for bb!

print(*' start, end, label'.split(), sep='\t')
ent_list_bb = []
for ent in doc_bb.ents:
    x = ent.label_
    ent_list_bb.append(x)

    print(ent.text, ent.label_,  sep='\t')
print('Make named entity visualization on 1 localhost...')
ent_freqs_bb = Counter(ent_list_bb)
df = pd.DataFrame.from_dict(ent_freqs_bb, orient='index')
df.plot(kind='bar')
# plt.set_title('NER label frequencies: Site 1')
plt.show()
displacy.serve(doc_bb, style='ent')

print('...or just save it as a file...')
svg = displacy.render(doc_bb, style='ent')
with open('ent_bb.svg', 'w', encoding='utf-8') as f:
    f.write(svg)


"""

#np plot idea 2
print(*' start, end, label'.split(), sep='\t')
ent_list_gd = []
for ent in doc_gd.ents:
    x = ent.label_
    ent_list_gd.append(x)

    print(ent.text, ent.label_,  sep='\t')
print('Make named entity visualization on 1 localhost...')
ent_freqs_gd = Counter(ent_list_gd)
df = pd.DataFrame.from_dict(ent_freqs_gd, orient='index')
df.plot(kind='bar')
# plt.set_title('NER label frequencies: Site 2')
plt.show()
displacy.serve(doc_gd, style='ent')


svg = displacy.render(doc_gd, style='ent')
with open('ent_gb.svg', 'w', encoding='utf-8') as f:
    f.write(svg)






print('Determine semantic similarities...')

print(f'    similarity between "{doc_bb}" and "{doc_gd}":')
print('    ', doc_bb.similarity(doc_gd))


input('Press [enter] to continue')

# scores = ner.predict([doc_bb, doc_gd])
print()
# print(scores)

