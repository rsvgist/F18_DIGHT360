print('''PRACTICE B

Write a script to get http://reynoldsnlp.com/scrape/aa.html and
save the source html to a local file.

''')
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://reynoldsnlp.com/scrape/aa.html")
with open('rnlp_aa.html', 'w') as f:
    print(driver.page_source, file=f)
driver.close()
input('Press [return] to continue.\n\n\n')



print('''PRACTICE C

Write a script to open https://www.google.com and search for `selenium-python tutorial`. Print the contents of each <cite> tag.

''')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("selenium-python tutorial")
elem.send_keys(Keys.RETURN)
for i, result in enumerate(driver.find_elements_by_xpath('//*/h3/a')):
    # print(i, dir(result), result.tag_name)
    print(result.get_attribute('href'))
input('Press [return] to close Chrome driver.')
driver.close()

