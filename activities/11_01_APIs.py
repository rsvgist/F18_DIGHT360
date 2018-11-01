"""In-class activities for 11-01 (APIs)."""

print('''
Future topics
    * Machine learning
        * Feature evaluation (for machine-learning)
    * Web scraping
        * Selenium browser driving
    * Natural Language Processing
        * Lemmatizing and stemming
        * Syntactic parsing
        * Topic modeling
        * Named entity recognition
        * Speech processing
    * Presenting results
        * Visualizations
    * Deeper with python
        * Classes/objects
        * Command line one-liners
        * Writing utilities (stdin, stdout, argv, etc.)
    * ???
''')
input('[return] to continue...\n')

print('''
API: Application Programming Interface

A set of clearly defined methods of communication between various software
components.

The existence of an API means that a website intends for you to use their data.

Most APIs require authentication, but for today we will focus on APIs that do
not.
''')

import json  # JavaScript Object Notation
from pprint import pprint  # pretty print
import requests as r


def get_swapi(url):
    """Get json data from StarWars API; return dict."""
    # Star Wars API (does not require authentication)
    response = r.get(url)
    return json.loads(response.text)


luke = get_swapi('https://swapi.co/api/people/1/')
print('This is the dict (not pretty printed):', luke)
print('Here is the name:', luke['name'])

for ship_url in luke['starships']:
    ship = get_swapi(ship_url)
    pprint(ship)


print('''

###############################################################################
PRACTICE A

Choose an API from
https://shkspr.mobi/blog/2016/05/easy-apis-without-authentication/
and write a function to get data from that API. Do something interesting with
the data you pulled.
''')
