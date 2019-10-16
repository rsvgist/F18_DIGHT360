from selenium import webdriver
from selenium.webdriver.common.keys import Keys



#specify path to chrome driver on windows
driver = webdriver.Chrome(executable_path='D:\python_projects\F18_DIGHT360\chromedriver.exe')

# driver.get("http://reynoldsnlp.com/scrape/aa.html")  # does not wait for AJAX
# with open('rnlp_aa.html', 'w') as f:
#     print(driver.page_source, file=f)
# input('Press [return] to continue.\n\n\n')
# input('Press [return] to close Chrome driver.')
# driver.close()








# driver.get("http://www.amazon.com/")  # does not wait for AJAX
# elem = driver.find_element_by_name("field-keywords")
# print('elem:', type(elem), elem)
# elem.clear()
# elem.send_keys("audio interface")
# elem.send_keys(Keys.RETURN)
# print(driver.page_source, '....')
# assert "No results found." not in driver.page_source
# input('Press [return] to close Chrome driver.')
# driver.close()


driver.get("http://www.google.com/")  # does not wait for AJAX
elem = driver.find_element_by_name("q")
print('elem:', type(elem), elem)
#solution
elem.clear()
elem.send_keys("selenium-python tutorial")
elem.send_keys(Keys.RETURN)
for i, result in enumerate(driver.find_elements_by_xpath('//*/h3/a')):
    # print(i, dir(result), result.tag_name)
    print(result.get_attribute('href'))
input('Press [return] to close Chrome driver.')
driver.close()