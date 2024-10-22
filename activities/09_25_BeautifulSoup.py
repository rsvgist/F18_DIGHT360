"""In-class activities for 09-25."""

print('Parsing HTML (for reals this time)')

# Regexes are not ideal HTML parsers
# In order to parse HTML, you need an HTML parser, such as beautifulsoup
print('https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start')
input('Press [enter] to continue')


###############################################################################
from bs4 import BeautifulSoup
import re

# open a previously saved HTML file and soupify it
with open('Healthcare_in_Canada-wikipedia.html', encoding= 'utf8') as healthy_file:
    soup = BeautifulSoup(healthy_file, 'html5lib')  # html5lib is the parser

print("Let's extract all of the links on this page...")
print('\tprinting just the first 10...')
for link in soup.find_all('a'):
    print(link.get('href'))
print()
input('Press [enter] to continue')

print("Let's find all the headers with <h2> tags in this article....")
print(soup.find_all('h2'))
print()
input('Press [enter] to continue')

print("Let's find all the <span> tags in this article with id=Public_opinion....")
print(soup.find_all('span', id='Public_opinion'))
print()
input('Press [enter] to continue')

print("Now find elements with 'poll' in the text....")
print(soup.find_all(string=re.compile(r'\bsingles\b', re.I)))
print()
input('Press [enter] to continue')
