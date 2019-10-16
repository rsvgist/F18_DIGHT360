"""Warm-up for 10-23."""

print('''WARMUP 1:

Import the data from 10_23_name_age_sport.csv and print the information in a
human-readable format:

'Rob is 37 and likes soccer.'
etc.''')



print('''WARMUP 2:

Create a dictionary using the data from 10_23_name_age_sport.csv:

    {'Rob': (37, 'soccer), 'Rachael': (38, 'ultimate frisbee'), ...}

How many different ways can you make this dictionary?
What is the most concise way you can come up with?''')


with open ('10_23_name_age_sport.csv') as datafile:
    name, age sport - line.rstrip().split(',')
    print(f'{name}) is {age} and likes {sport}.')

with open ('10_23_name_age_sport.csv') as datafile:
    d = {}
    for line in datafile:
        name, age, sport = line.rstrip().split(','
        d[name]) = (int(age),sport)

with open ('10_23_name_age_sport.csv') as datafile:
    lines = datafile.readlines()
    d = {for i in datafile}

   
   
   
{n: (int(a) s) for n, a, s, in [line.rstrip().split(',') for line in lines]}


#in 1 line!!! dang
 {n: (int(a), s) for n, a, s, in [line.rstrip().split(',') for line in open('10_23_name_age_sport.csv')]}
