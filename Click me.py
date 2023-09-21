import random, pyautogui as pyauto
for i in range(15):
    h = random.randint(0, 1080)
    w = random.randint(0, 1920)
    pyauto.click(h, w, duration= 0.3)
    pyauto.hotkey('winleft', 'm')

import time, rotatescreen as rs
pd = rs.get_primary_display()
angel_list = [90, 180, 270, 0]
for i in range(5):
    for x in angel_list:
        pd.rotate_to(x)
        time.sleep(0.5)
