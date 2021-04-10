import rpa as r
import pyautogui as p
r.init()
r.url('http://www.google.com')

r.wait(2.0)

r.type('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input', 'lubrificador para sexo anal[enter]')

r.wait(2.0)

r.snap('page', 'rpa_search.png')
r.wait(2.0)
r.close()
