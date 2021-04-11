import pyautogui as p

p.doubleClick(x=26, y=337)

p.sleep(4)

p.write('www.udemy.com')
p.press('enter')
p.sleep(3)


local_search = p.locateOnScreen('Pesquisa.png', confidence=.9)
local_search = p.center(local_search)

print(local_search)
xSearch, ySearch = local_search


p.moveTo(xSearch, ySearch, duration=1)
p.click(xSearch, ySearch)
p.sleep(1)
p.write("Miller")
p.press('enter')
p.sleep(3)
p.screenshot('loco.png')
p.sleep(3)