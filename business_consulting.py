from selenium.webdriver import Chrome
import time as t

navigator = Chrome()

navigator.get('https://consultacnpj.com/cnpj/')
navigator.maximize_window()
t.sleep(3)

cnpjs = ['45997418000153', '72273196001090', '33000167000101']

for item in cnpjs:
    input_site = navigator.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div/div/div/div/div[2]/div/div/input')
    input_site.clear()
    input_site.send_keys(item)
    t.sleep(2)
    data = navigator.find_element_by_xpath('//*[@id="company-data"]')
    with open(f'{str(item)}.csv', 'w', encoding='UTF-8') as csv:
        csv.write(data.text)
    t.sleep(2)

navigator.quit()

