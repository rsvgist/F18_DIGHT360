"""In-class activities for 12-06."""

# Install: python3 -m pip install spacy && python3 -m spacy download en

print('importing spacy...')
import spacy
from spacy import displacy

print('Load English tokenizer, tagger, parser, NER and word vectors...')
nlp = spacy.load('en')
print('nlp:', type(nlp), dir(nlp))


MC_DIR = 'D:\\python_projects\\F18_DIGHT360\\assignments\\final_grammy_noms_clean.txt'

print('Process a document...')
with open(MC_DIR, encoding='utf-8') as f:
    pledge = f.read()
doc = nlp(pledge)
print('doc:', type(doc), dir(doc))

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

print(*'token, start, end, label'.split(), sep='\t')
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_, sep='\t')
print('Make named entity visualization on localhost...')
displacy.serve(doc, style='ent')

print('...or just save it as a file...')
svg = displacy.render(doc, style='ent')
with open('ent_ex.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print('Determine semantic similarities...')
doc1 = nlp('the fries were gross')
doc2 = nlp('worst fries ever')
print(f'    similarity between "{doc1}" and "{doc2}":')
print('    ', doc1.similarity(doc2))

print('Determine semantic similarities...')
doc1 = nlp('Pizza is not my friend')
doc2 = nlp('Pizza has cheese')
print(f'    similarity between "{doc1}" and "{doc2}":')
print('    ', doc1.similarity(doc2))

