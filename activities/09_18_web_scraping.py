"""In-class activities for 09-21."""

# Review namespace on assignment_1.py and assignment_1_eval.py
# precision and recall
# Web scraping

###############################################################################
print('namespace with assignment_1.py and assignment_1_eval.py\n\n')

###############################################################################
print('Precision and recall\n\n')

# When you report accuracy at classifying something, precision and recall are
# commonly-used metrics.
# https://en.wikipedia.org/wiki/Precision_and_recall
# tp = True Positive
# tn = True Negative
# fp = False Positive
# fn = False Negative

# Precision = tp / (tp + fp)  # of all the positives, how many were correct?
# Recall = tp / (tp + fn)  # of all the trues, how many were identified?


###############################################################################
print('Ethics of web scraping')
print()
# https://medium.com/towards-data-science/ethics-in-web-scraping-b96b18136f01

###############################################################################
print('brief introduction to HTML\n\n')

"""
HTML is a markup language that defines document content/structure:
learn as much as you want here:
https://www.w3schools.com/html/html_intro.asp
https://www.w3schools.com/html/html_basic.asp

For our purposes, you just need to know that there are lots of different
elements in HTML with start tags and end tags. The end tag is exactly like
the start tag, but with a slash: <p>This is a paragraph.</p>

HTML elements can nest, but to be well-formed a nested element must close
before its parent: <h1>This heading has a <p>paragraph in it.</p></h1>
NOT well-formed:   <h1>This heading has a <p>paragraph in it.</h1></p>

Technically, regular expressions cannot parse HTML. Elements can nest
infinitely, but that would require an infinitely long regular expression,
because they have no mechanism ("stack") to keep track of what they have seen.

For example, '<div>.*</div>' (with the re.DOTALL flag) will capture everything
in the text below except the final </div> tag. There is no way to pair open tags
with their close tags unless they are hardcoded.

<div>The parent div element.
    <div>The child div element.
    </div>
</div>
Theoretical background: https://en.wikipedia.org/wiki/Chomsky_hierarchy
Must-read: https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454

HOWEVER, regular expressions CAN be used to quickly find a relevant part of
HTML.

The BEST way is to use a real HTML parser, which we will do later.
"""

###############################################################################
# Using browser developer tools to explore HTML

###############################################################################
# Using regex to pseudo-parse HTML

# In a browser open a webpage:
# https://www.rd.com/jokes/halloween-jokes-for-kids/
# ...then View Source, then search for 'Mummy' in the source
# each joke is contained in an <article> tag
# the joke title is inside the <h2> tag
# the joke itself is inside a <p> tag inside a <div> tag with `class="content-wrapper"`

# PRACTICE 1
# Copy and paste the 1st 10 jokes to regex101.com or pythex.org (each joke is
# everything from <article> to </article>)
#   a) write a regular expression to capture all the `<article>`s
#   b) modify the regex to capture the title of each joke using a group
#   c) modify the regex to capture the joke itself, too
#   d) modify the regex to capture the Q and the A part of the joke separately

###############################################################################
# Retrieving a webpage

# We can use the requests module to pull the source of a webpage into
# a string object.

import requests as r

joke_url = 'https://www.rd.com/jokes/halloween-jokes-for-kids/'
headers = {'user-agent': 'Robert Reynolds (robert_reynolds@byu.edu)'}
response = r.get(joke_url, headers=headers)
print(response.text[:100], '....')
print()

# PRACTICE 2
# Write a script to pull the html and pseudo-parse it with a regex to extract
# the joke titles, the Q and the A. I recommend using re.findall().


###############################################################################
print('Query strings')
print()

# When you type in `spam` on google.com and hit [return], it pulls up a new
# page with a url like this:
# https://www.google.com/search?q=spam&oq=spam&aqs=chrome..69i57j0l5.3641j0j8&sourceid=chrome&ie=UTF-8
# Everything after the `?` is query strings with the following key/value pairs
# q         spam
# oq        spam
# aqs       chrome..69i57j0l5.3641j0j8
# sourceid  chrome
# ie        UTF-8

# You can construct urls inside python to get search results:

import random
import requests as r
import time

comics_responses = []
google = 'https://www.google.com/search?q='
for term in ['xkcd', 'smbc', 'calvin+and+hobbes']:
    comics_responses.append(r.get(google + term, headers=headers))
    time.sleep(random.uniform(1.5, 2.5))  # Let the server breathe
for each_response in comics_responses:
    print('Do stuff with those websites here...')

# NOTE!!!!! Without time.sleep(), the code above would be extremely impolite,
# and many servers would immediately block your ip address! It sends requests as
# fast as python can function, which can overload a server, and is essentially
# what a DDoS attack consists of.
