import time

import pyautogui
#https://www.cnblogs.com/suanmiaoup/p/12389412.html 教程可以看下这个

#操作需要两步，第一步：将test.log写入到文件名的输入框内，
input('继续')
time.sleep(10)
pyautogui.write(r"F:\python\pyauto_gui\study\3.png")
#第二步，敲回车：相当于点击【打开】按钮，


pyautogui.press('enter', presses=2)
#注意：这里presses要2次才能生效。