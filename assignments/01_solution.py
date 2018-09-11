"""One POSSIBLE solution to Assignment 1."""

from assignment_1_eval import evaluate

no_pl_nouns = ['news', 'gymnastics', 'economics', 'mathematics', 'statistics',
               'luggage', 'baggage', 'furniture', 'information']

irr_dict = {'fish': 'fish',
            'sheep': 'sheep',
            'barracks': 'barracks',
            'foot': 'feet',
            'tooth': 'teeth',
            'goose': 'geese',
            'child': 'children',
            'man': 'men',
            'woman': 'women',
            'person': 'people',
            'mouse': 'mice',
            'deer': 'deer',
            'corpus': 'corpora',
            'genus': 'genera'}
vowels = ['a', 'e', 'i', 'o', 'u']


def pluralize(sg):  # perfect RECALL, not great PRECISION
    """Return list of plural form(s) of input_word.

    Building this function is the purpose of Assignment 1.
    The most basic case is already provided.
    """
    if sg in irr_dict:
        return[irr_dict[sg]]
    if sg in no_pl_nouns:
        return ['']  # no plural possible, so skip everything else
    if sg.endswith('is'):
        return [sg[:-2] + 'es']
    if sg.endswith('on'):
        return [sg[:-2] + 'a']
    if sg.endswith('um'):
        return [sg[:-2] + 'a', sg + 's']
    if sg.endswith('us') and len(sg) > 3:  # checking length rules out bus
        return [sg[:-2] + 'i', sg + 'es']
    if sg.endswith('a'):
        return [sg + 'e', sg + 's']
    if sg.endswith('f'):
        return [sg[:-1] + 'ves']
    if sg.endswith('fe'):
        return [sg[:-2] + 'ves']
    if sg.endswith('o'):
        return[sg + 's', sg + 'es']
    if sg.endswith('ex') or sg.endswith('ix'):
        return [sg[:-2] + 'ices', sg + 'es']
    if sg[-1] in ['x', 's', 'z']:
        return [sg + 'es']
    if sg.endswith('ch'):
        return [sg + 'es']
    if sg.endswith('y') and sg[-2] not in vowels:
        return [sg[:-1] + 'ies']
    return [sg + 's']


print('evaluate...')
evaluate(pluralize)
