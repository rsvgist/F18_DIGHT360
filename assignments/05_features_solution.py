"""Extract 3+ features from Mini-CORE corpus."""

from glob import glob
import re
from string import punctuation as punct  # string of common punctuation chars

import nltk

MC_DIR = 'D:\\python_projects\\F18_DIGHT360\\assignments\\Mini-CORE\\'
print(f'Exporting features from files in `{MC_DIR}`...')


def clean(in_file):
    """Remove headers from corpus file. Otherwise, remove <h> and <p> tags."""
    out_str = ''
    for line in in_file:
        if re.match(r'<[hp]>', line):
            out_str += re.sub(r'<[hp]>', '', line) + ' '
    return out_str


def subcorp(name):
    """Extract subcorpus from filename.

    name -- filename

    The subcorpus is the first abbreviation after `1+`.
    """
    return name.split('+')[1]


def ttr(in_Text):
    """Compute type-token ratio for input Text.

    in_Text -- nltk.Text object or list of strings
    """
    return len(set(in_Text)) / len(in_Text)


def pro1_tr(in_Text):
    """Compute 1st person pronoun-token ratio for input Text.

    in_Text -- nltk.Text object or list of strings
    """
    pro1_count = len([i for i in in_Text
                      if re.match(r'(?:i|me|my|mine)$', i, re.I)])
    return pro1_count / len(in_Text)


def pro2_tr(in_Text):
    """Compute 2nd person pronoun-token ratio for input Text.

    in_Text -- nltk.Text object or list of strings
    """
    pro2_count = len([i for i in in_Text
                      if re.match(r'(?:ye|you(?:rs?)?)$', i, re.I)])
    return pro2_count / len(in_Text)


def pro3_tr(in_Text):
    """Compute 3rd person pronoun-token ratio for input Text.

    in_Text -- nltk.Text object or list of strings
    """
    pro3_count = len([i for i in in_Text
                      if re.match(r'(?:s?he|its?|hi[ms]|hers?)$', i, re.I)])
    return pro3_count / len(in_Text)


def punct_tr(in_Text):
    """Compute punctuation-token ratio for input Text.

    in_Text -- nltk.Text object or list of strings
    """
    punct_RE = '[' + punct + ']+$'
    punct_count = len([i for i in in_Text if re.match(punct_RE, i)])
    return punct_count / len(in_Text)


with open('05_output.tsv', 'w') as out_file:
    print('filename', 'ttr', '1st-pro', '2nd-pro', '3rd-pro', 'punct',
          'subcorpus', sep='\t', file=out_file)
    print('Extracting features...')
    for f in glob(MC_DIR + '*.txt'):
        # show progress by printing dots and print every hundredth number
        print('.', end='', flush=True)
        # open the file
        with open(f) as the_file:
            raw_text = clean(the_file)
        tok_text = nltk.word_tokenize(raw_text)
        print(f, ttr(tok_text), pro1_tr(tok_text), pro2_tr(tok_text),
              pro3_tr(tok_text), punct_tr(tok_text), subcorp(f),
              sep='\t', file=out_file)
    print()  # newline after progress dots
