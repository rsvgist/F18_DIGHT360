"""In-class activities for 09-20."""

# WARMUP
# https://regexone.com/

# Reading and writing files

###############################################################################
print('Reading and writing files...')

print('Opening and printing jokes.txt...')
joke_file = open('jokes.txt', 'r')  # 'r' = read mode
# identical to joke_file = open('jokes.txt')  # r=read mode; default
for line in joke_file:
    print(line)
print()

print('Writing test_file.txt...')
# not the best way, usually
my_file = open('test_file.txt', 'w')  # 'w' = overwrite mode
print('Hello file!', file=my_file)  # or my_file.write('Hello file!\n')
# Notice that the end `\n` is automatic with `print`, but not file.write()
my_file.close()  # not the best way, usually
print()

print('Adding another line to test_file.txt using `with`...')
# the "best" way to open (and automatically close) files is using `with`:
with open('test_file.txt', 'a') as my_file:  # 'a' = append mode
    print('Goodbye, file!', file=my_file)
# once the indented code block is executed, the file is automatically closed
print()

print('PRACTICE A')
print('''Write a loop that writes 3 files: file0.txt, file1.txt, file2.txt. The
contents of file0.txt should be "This is file0.txt".''')
input('Press [enter] to continue')

###############################################################################
# Using browser developer tools to explore HTML
# `Inspect`

###############################################################################
# Retrieving a webpage

# We can use the requests module to pull the source of a webpage into
# a string object.

import requests as r

joke_url = 'https://www.rd.com/jokes/halloween-jokes-for-kids/'
h = {'user-agent': 'Robert Reynolds (robert_reynolds@byu.edu)'}
response = r.get(joke_url, headers=h)
print(response.text)
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
    print(each_response.text)

# NOTE!!!!! Without time.sleep(), the code above would be extremely impolite,
# and many servers would immediately block your ip address! It sends requests as
# fast as python can function, which can overload a server, and is essentially
# what a DDoS attack consists of.
