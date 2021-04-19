import pandas as pd
import pyautogui as p
import rpa as r
import pandas as pds

r.init()
r.url('http://rpachallenge.com')

p.sleep(10)

r.download('http://rpachallenge.com/assets/downloadFiles/challenge.xlsx', 'challenge.xlsx')

p.sleep(1)

data = pds.read_excel('challenge.xlsx', sheet_name='Sheet1')

df = pd.DataFrame(data, columns=['First Name', 'Last Name ', 'Company Name', 'Role in Company', 'Address', 'Email', 'Phone Number'])

r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')

for row in df.itertuples():
    r.type('//*[@ng-reflect-name="labelFirstName"]', row[1])
    r.type('//*[@ng-reflect-name="labelLastName"]', row[2])
    r.type('//*[@ng-reflect-name="labelCompanyName"]', row[3])
    r.type('//*[@ng-reflect-name="labelRole"]', row[4])
    r.type('//*[@ng-reflect-name="labelAddress"]', row[5])
    r.type('//*[@ng-reflect-name="labelEmail"]', row[6])
    r.type('//*[@ng-reflect-name="labelPhone"]', str(row[7]))
    r.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')

p.sleep(5)

p.screenshot('score.png')

r.close()

