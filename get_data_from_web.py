import rpa as r
import pyautogui as p
import pandas as pd
import os as o

r.init()
r.url('https://rpachallengeocr.azurewebsites.net/')
p.sleep(7)

count_page = 1

while count_page <= 3:
    r.table('//*[@id="tableSandbox"]', 'temp.csv')
    data_csv = pd.read_csv('temp.csv')
    if count_page == 1:
        data_csv.to_csv(r'webTable.csv', mode='a', index=None, header=True)
    else:
        data_csv.to_csv(r'webTable.csv', mode='a', index=None, header=False)
    r.click('//*[@id="tableSandbox_next"]')
    count_page += 1

r.close()
o.remove('temp.csv')


