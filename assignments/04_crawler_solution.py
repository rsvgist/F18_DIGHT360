"""Iteratively scrape reynoldsnlp.com/scrape/."""

from glob import glob
import random
import requests as r
import time

from bs4 import BeautifulSoup


def get_rnlp(filename):
    """Scrape html file from reynoldsnlp.com/scrape/; write to file."""
    time.sleep(random.uniform(1.5, 2.5))
    print('Requesting {}....'.format(filename))
    headers = {'user-agent': 'Robert Reynolds (robert_reynolds@byu.edu)'}
    req = r.get('http://reynoldsnlp.com/scrape/' + filename, headers=headers)
    with open('scrape/' + filename, 'w') as html_file:
        html_file.write(req.text)


def get_hrefs(filename):
    """Return list of href values from all <a> tags in `filename`."""
    assert filename.endswith('.html')
    print('Extracting hrefs from {}....'.format(filename))
    with open('scrape/' + filename) as html_file:
        soup = BeautifulSoup(html_file, 'html5lib')
    return [link.get('href').split('/')[-1] for link in soup.find_all('a')]


todo = ['aa.html']  # seed url
done = set()
while len(todo) > 0:
    fname = todo.pop()
    if fname not in done:
        get_rnlp(fname)
        new_hrefs = get_hrefs(fname)
        done.add(fname)
        todo.extend(new_hrefs)

print(sorted([u.split('/')[-1][:2] for u in glob('scrape/*.html')]))
