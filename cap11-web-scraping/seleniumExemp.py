
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://mail.yahoo.com')


# try:
#     elem = browser.find_element_by_class_name('bookcover')
#     print('Encontrado elemento %s com esse nome de classe!' % (elem.tag_name))
# except:
#     print('Nao foi encontrado nenhum elemento com esse nome')

# linkElem = browser.find_element_by_link_text('Read It Online')
# linkElem.click()