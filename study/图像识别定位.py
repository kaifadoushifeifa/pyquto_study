# 导入库
import time

import pyautogui
from ZdxAutoGui import ZdxAutoGui
# 寻找截图所在位置
# location = pyautogui.locateCenterOnScreen(r'F:\python\pyauto_gui\study\start_button.png',confidence=0.8,grayscale=True)
# location = pyautogui.locateOnScreen('start_button.png',confidence=0.8,grayscale=True)
import pyperclip

location = pyautogui.locateCenterOnScreen('test2.png',confidence=0.9)
# 打印截图所在位置
# 鼠标移动到（114，514）坐标,过程持续3秒
pyautogui.moveTo(*location, 3)
pyautogui.moveRel(xOffset=-50,yOffset=-50,duration=0.4)
pyautogui.click()
ZdxAutoGui.write_ch('你在干嘛呢')
ZdxAutoGui.enter()
location = pyautogui.locateCenterOnScreen('touxiang.png',confidence=0.9)
pyautogui.moveTo(*location, 3)
pyautogui.click()
ZdxAutoGui.write_ch('在么')
ZdxAutoGui.enter()
# 输出结果
# Point(x=1547, y=1563)



# def test1():
#     >> > t = locateOnScreen('images/test1.png', region=(0, 940, 1919, 939))
#     >> > print(center(t))
#
#     Point(x=873, y=1056)