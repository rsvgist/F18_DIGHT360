"""In-class activities for 04-18."""

print("""
### INSTALLATION ###
http://selenium-python.readthedocs.io/installation.html

$ pip3 install selenium

Download driver:
    http://selenium-python.readthedocs.io/installation.html#drivers
Save the driver in /usr/local/bin/ (or /usr/bin/)
    ...or just save it in the same folder as your selenium script.
""")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")  # does not wait for AJAX
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
print('elem:', type(elem), elem)
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print(driver.page_source[:200], '....')
assert "No results found." not in driver.page_source
input('Press [return] to close Chrome driver.')
driver.close()


print('''PRACTICE A

Install selenium and run this script.

''')
input('Press [return] to continue.\n\n\n')

print('''PRACTICE B

Write a script to get http://reynoldsnlp.com/scrape/aa.html and
save the source html to a local file.

''')
input('Press [return] to continue.\n\n\n')


print('''PRACTICE C

Write a script to open https://www.google.com and search for `selenium-python
tutorial`. Print the contents of each <cite> tag.
(see http://selenium-python.readthedocs.io/locating-elements.html)

''')
input('Press [return] to continue.\n\n\n')


