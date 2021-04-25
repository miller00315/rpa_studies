from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t


chrome_navigator = Chrome()
chrome_navigator.get('https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login')

chrome_navigator.maximize_window()

t.sleep(1)

chrome_navigator.find_element_by_xpath("//map/area[2]").click()

t.sleep(3)

chrome_navigator.find_element_by_name('ExpressaoPesquisa').send_keys("03768202000176")

t.sleep(1)

chrome_navigator.find_element_by_xpath('//select[2]/option[4]').click()

t.sleep(1)

chrome_navigator.find_element_by_css_selector('input[type="submit"]').click()

t.sleep(3)

chrome_navigator.quit()
