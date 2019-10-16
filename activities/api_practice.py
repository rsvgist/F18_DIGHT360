"""In-class activities for 11-01 (APIs)."""


import json  # JavaScript Object Notation
from pprint import pprint  # pretty print
import requests as r


def get_swapi(url): # sw-api
    
    response = r.get(url)
    return json.loads(response.text)


ships = get_swapi('https://swapi.co/api/starships/?search=fighter') # search query- starships w/ 'fighter'



#print the results of each ship w/ 'fighter' query
for i in range(6):
    print('Ship ', i,': ')
    print('name: ',ships['results'][i]['name'])
    print('manufacturer: ',ships['results'][i]['manufacturer'])


"""
print('''

###############################################################################
PRACTICE A

Choose an API from
https://shkspr.mobi/blog/2016/05/easy-apis-without-authentication/
and write a function to get data from that API. Do something interesting with
the data you pulled.
''')
"""
