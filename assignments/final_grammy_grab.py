#scrape from hw 3

# scraping w/ one request - don't need sleep for single request
# import lib
import requests as r
from bs4 import BeautifulSoup
import re


# data_url = 'https://www.billboard.com/articles/news/grammys/8489045/2019-grammy-nominees-full-list'
# data_url = 'https://www.goldderby.com/article/2018/2019-grammy-nominations-list-nominees-61st-grammys-news/'
# 
data_url = 'https://www.grammy.com/grammys/awards/winners-nominees/140'
h = {'user-agent': 'Paul Russavage (paul.rsvg@byu.edu)'}
response = r.get(data_url, headers=h)

# check encoding
print(response.encoding)
# write response to file
with open('grammys_all_yrs.html', 'w', encoding='utf-8') as my_file:  # 'w' = write mode
    print(response.text, file=my_file)
# close file, print msg
print('file written:',  response.text[:200], '....')

#now parse that file with bs4



# soup = BeautifulSoup(txt, "html.parser")
# print("".join(soup.strings))


# open a previously saved HTML file and soupify it
with open('grammys_all_yrs.html', encoding= 'utf8') as healthy_file:
    soup = BeautifulSoup(healthy_file, 'html5lib')  # html5lib is the parser

tags = soup.find_all(['h3', 'p'])



print("Let's find all the headers with <h2> tags in this article....")
print(soup.find_all('h2'))
print()
input('Press [enter] to continue')

print("Let's find the class w/ the whole article listing the grammy noms")
print(soup.find_all('div', class_='article_content'))
print()
input('Press [enter] to continue')


"""
x = str(soup.find_all('p'))
content = str(re.sub("<.*?>", "", x))
print(content)
"""

# save article data to new file w mostly just text
article = str(soup.find_all(['h3', 'p']))
content = str(re.sub("<.*?>", "", article))
# write response to file
with open('final_grammynoms_61_clean.txt', 'w', encoding= 'utf8') as my_file2:  # 'w' = write mode
    print(content, file=my_file2)
# finishing msg
print('grammy list parsed to new file...')
print(content[:200])
input('Press [enter] to continue')

"""
#categories
re.match(r'<strong>(.+?)</strong')

number and genre
re.match(r'<strong>Category(.+?)</strong')

song and artist
<p>•.*?<br/>.*?<br/>

re.match(r'')

re.match(r'')

re.match(r'')
"""
"""
# save article data to new file w/ some p/em tags
article = soup.find_all('p')
# write response to file
with open('final_grammy_noms_parsed.txt', 'w', encoding= 'utf8') as my_file2:  # 'w' = write mode
    print(article, file=my_file2)
# finishing msg
print('grammy list parsed to new file...')
input('Press [enter] to continue')

def clean(in_file):
   
    out_str = ''
    for line in in_file:
        if re.match(r'<[p]>', line):
            out_str += re.sub(r'<[p]>', '', line)
    return out_str



from bs4 import BeautifulSoup
soup = BeautifulSoup(''.join(text))
for i in soup.prettify().split('<p>'):
    print '<strong>' + ''.join(i)

"""
"""
# import lib
import re
# open file
with open('football.html') as my_file:
    # stop at 1166 lines to make regex parsing easier
    head = [next(my_file) for x in range(1166)]
# convert to string
header = str(head)
# run regex
players = re.findall(r'<tr.*?<td.*?/s.*?<a.*?>(.+?)</a>.*?</td>', header)
print(players)
# write response to file
with open('football_parsed.txt', 'w') as my_file2:  # 'w' = write mode
    print(players, file=my_file2)
# finishing msg
print('player list parsed to new file...')

#from hw 4

from glob import glob
import requests as r
import time
from bs4 import BeautifulSoup
def get_rnlp(filename):
    time.sleep(2)   # wait 2 sec btw each request
    h = {'user-agent': 'Paul R. (paul.rsvg@byu.edu)'}
    req = r.get('http://reynoldsnlp.com/scrape/' + filename, headers=h)
    with open('scrape/' + filename, 'w') as page:
        page.write(req.text)
def get_hrefs(filename):
    assert filename.endswith('.html')
    with open('scrape/' + filename) as page:
        parsed = BeautifulSoup(page, 'html5lib')
    return [link.get('href').split('/')[-1] for link in parsed.find_all('a')]
atag = ['aa.html']  # seed url
all_atags = set()
while len(atag) > 0:
    fname = atag.pop()
    if fname not in all_atags:
        get_rnlp(fname)
        add_hrefs = get_hrefs(fname)
        all_atags.add(fname)
        atag.extend(add_hrefs)
print(sorted([u.split('/')[-1][:2] for u in glob('scrape/*.html')]))
"""