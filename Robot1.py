import pyautogui as p

print(p.position())

p.sleep(2)
p.moveTo(240, 81, duration=1)
p.click(240, 81)
p.sleep(1)
p.typewrite('www.google.com.br')
p.sleep(1)
p.press('enter')
p.sleep(1)
