import pyautogui, time 

time.sleep(20)   # timp pentru start
f = open('text.txt', 'r')
for word in f:
    pyautogui.typewrite(word)
    time.sleep(6)  #un mesaj la fiecare 6 secunde 
    pyautogui.press('enter') 
