"""Singular-plural pairs to be used for evaluating Assignment 1."""

from collections import defaultdict  # just like dict, but returns default if key not found  # noqa

pairs = [('snake', 'snakes'),
         ('window', 'windows'),
         ('box', 'boxes'),
         ('boy', 'boys'),
         ('lorry', 'lorries'),
         ('potato', 'potatoes'),
         ('knife', 'knives'),
         ('girl', 'girls'),
         ('window', 'windows'),
         ('witch', 'witches'),
         ('gas', 'gases'),
         ('bus', 'buses'),
         ('kiss', 'kisses'),
         ('way', 'ways'),
         ('baby', 'babies'),
         ('hero', 'heroes'),
         ('echo', 'echoes'),
         ('embargo', 'embargoes'),
         ('tomato', 'tomatoes'),
         ('torpedo', 'torpedoes'),
         ('veto', 'vetoes'),
         ('auto', 'autos'),
         ('kangaroo', 'kangaroos'),
         ('kilo', 'kilos'),
         ('memo', 'memos'),
         ('photo', 'photos'),
         ('piano', 'pianos'),
         ('pimento', 'pimentos'),
         ('pro', 'pros'),
         ('solo', 'solos'),
         ('soprano', 'sopranos'),
         ('studio', 'studios'),
         ('tattoo', 'tattoos'),
         ('video', 'videos'),
         ('zoo', 'zoos'),
         ('buffalo', 'buffalos'),
         ('buffalo', 'buffaloes'),
         ('cargo', 'cargos'),
         ('cargo', 'cargoes'),
         ('halo', 'halos'),
         ('halo', 'haloes'),
         ('mosquito', 'mosquitos'),
         ('mosquito', 'mosquitoes'),
         ('motto', 'mottos'),
         ('motto', 'mottoes'),
         ('no', 'nos'),
         ('no', 'noes'),
         ('tornado', 'tornados'),
         ('tornado', 'tornadoes'),
         ('volcano', 'volcanos'),
         ('volcano', 'volcanoes'),
         ('zero', 'zeros'),
         ('zero', 'zeroes'),
         ('knife', 'knives'),
         ('leaf', 'leaves'),
         ('hoof', 'hooves'),
         ('life', 'lives'),
         ('self', 'selves'),
         ('elf', 'elves'),
         ('fish', 'fish'),
         ('sheep', 'sheep'),
         ('barracks', 'barracks'),
         ('foot', 'feet'),
         ('tooth', 'teeth'),
         ('goose', 'geese'),
         ('child', 'children'),
         ('man', 'men'),
         ('woman', 'women'),
         ('person', 'people'),
         ('mouse', 'mice'),
         ('deer', 'deer'),
         ('alga', 'algae'),
         ('amoeba', 'amoebae'),
         ('amoeba', 'amoebas'),
         ('antenna', 'antennae'),
         ('antenna', 'antennas'),
         ('formula', 'formulae'),
         ('formula', 'formulas'),
         ('larva', 'larvae'),
         ('nebula', 'nebulae'),
         ('nebula', 'nebulas'),
         ('vertebra', 'vertebrae'),
         ('corpus', 'corpora'),
         ('genus', 'genera'),
         ('alumnus', 'alumni'),
         ('bacillus', 'bacilli'),
         ('cactus', 'cacti'),
         ('cactus', 'cactuses'),
         ('focus', 'foci'),
         ('fungus', 'fungi'),
         ('fungus', 'funguses'),
         ('nucleus', 'nuclei'),
         ('octopus', 'octopi'),
         ('octopus', 'octopuses'),
         ('radius', 'radii'),
         ('stimulus', 'stimuli'),
         ('syllabus', 'syllabi'),
         ('syllabus', 'syllabuses'),
         ('terminus', 'termini'),
         ('addendum', 'addenda'),
         ('bacterium', 'bacteria'),
         ('curriculum', 'curricula'),
         ('curriculum', 'curriculums'),
         ('datum', 'data'),
         ('erratum', 'errata'),
         ('medium', 'media'),
         ('memorandum', 'memoranda'),
         ('memorandum', 'memorandums'),
         ('ovum', 'ova'),
         ('stratum', 'strata'),
         ('symposium', 'symposia'),
         ('symposium', 'symposiums'),
         ('apex', 'apices'),
         ('apex', 'apexes'),
         ('appendix', 'appendices'),
         ('appendix', 'appendixes'),
         ('cervix', 'cervices'),
         ('cervix', 'cervixes'),
         ('index', 'indices'),
         ('index', 'indexes'),
         ('matrix', 'matrices'),
         ('matrix', 'matrixes'),
         ('vortex', 'vortices'),
         ('analysis', 'analyses'),
         ('axis', 'axes'),
         ('basis', 'bases'),
         ('crisis', 'crises'),
         ('diagnosis', 'diagnoses'),
         ('emphasis', 'emphases'),
         ('hypothesis', 'hypotheses'),
         ('neurosis', 'neuroses'),
         ('oasis', 'oases'),
         ('parenthesis', 'parentheses'),
         ('synopsis', 'synopses'),
         ('thesis', 'theses'),
         ('criterion', 'criteria'),
         ('phenomenon', 'phenomena'),
         ('automaton', 'automata'),
         ('news', ''),
         ('gymnastics', ''),
         ('economics', ''),
         ('mathematics', ''),
         ('statistics', ''),
         ('luggage', ''),
         ('baggage', ''),
         ('furniture', ''),
         ('information', '')]

# dicts that map sg to list of pl, and pl to list of sg
sgpl_dict = defaultdict(list)
plsg_dict = defaultdict(list)
for sg, pl in pairs:
    sgpl_dict[sg].append(pl)
    plsg_dict[pl].append(sg)


def evaluate_old(pl_func, pair_data=pairs):
    """Evaluate the performance of pluralize function based on pairs data.

    pl_func -- function that pluralizes input word (default=pluralize)
    pair_data -- list of 2-tuples: [(sg1, pl1), (sg2, pl2),...] (default=pairs)
    """
    total = len(pair_data)
    # Determine how many lexemes have more than one plural form.
    # duplicates = len(set([i for i, j in pair_data]))
    correct = 0
    for sg, pl in pair_data:
        predicted_pl = pl_func(sg)
        if pl in predicted_pl:
            correct += 1
            print('correct:', sg, predicted_pl, '({})'.format(pl), sep='\t')
        else:
            print('INcorrect:', sg, predicted_pl, '({})'.format(pl), sep='\t')
    print('Your score:', correct, '/', total, '{:.2%}'.format(correct / total))


def evaluate(func, input_type='sg'):
    """Evaluate the performance of pluralize function based on pairs data.

    func -- function that changes input word (default=pluralize)
    input_type -- 'sg' or 'pl'
    """
    print(f'Evaluating the function {func.__name__} ...')
    assert input_type in ['sg', 'pl']
    if input_type == 'sg':
        pair_dict = sgpl_dict
    elif input_type == 'pl':
        pair_dict = plsg_dict
    total = len(pair_dict)
    # Determine how many lexemes have more than one plural form.
    # duplicates = len(set([i for i, j in pair_data]))
    correct = 0
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for k, v in pair_dict.items():
        gold = set(v)
        predicted = set(func(k))
        if gold == predicted or (gold == {''} and predicted == set()):
            print('correct:', k, '/'.join(predicted), sep='\t')
            tp += len(gold)
            correct += 1
            continue
        else:
            print('INcorrect:', k, '/'.join(predicted),
                  '(should be {})'.format('/'.join(gold) or []), sep='\t')
        fp += len(predicted.difference(gold))
        fn += len(gold.difference(predicted))
        tp += len(predicted.intersection(gold))
        if len(gold) == 0 and len(predicted) == 0:
            tn += 1
    print('accuracy:', correct, '/', total, '{:.2%}'.format(correct / total),
          '(for how many words did you get all plurals correct?)')
    print('precision:', tp, '/', tp + fp, '{:.2%}'.format(tp / (tp + fp)),
          '(of all predicted plurals, how many are correct?)')
    print('recall:', tp, '/', tp + fn, '{:.2%}'.format(tp / (tp + fn)),
          '(of all correct plural forms, how many do you predict?)')
