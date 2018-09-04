"""Template for Assignment 1."""

from collections import defaultdict

from assignment_1_eval import evaluate

irr_dict = {'tooth': 'teeth',  # use this dictionary SPARINGLY
            'genus': 'genera'}


def pluralize(sg):
    """Return list of plural form(s) of input_word.

    Building this function is the purpose of Assignment 1.
    The most basic case is already provided.
    """
    plurals = []
    if sg in irr_dict:
        return[irr_dict[sg]]
    elif sg.endswith('on'):
        plurals.append(sg[-2:] + 'a')
    else:
        plurals.append(sg + 's')
    return [sg + 's']


if __name__ == '__main__':
    evaluate(pluralize)
