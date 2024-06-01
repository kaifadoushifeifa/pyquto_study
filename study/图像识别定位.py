# 导入库
import pyautogui

# 寻找截图所在位置
# location = pyautogui.locateCenterOnScreen(r'F:\python\pyauto_gui\study\start_button.png',confidence=0.8,grayscale=True)
# location = pyautogui.locateOnScreen('start_button.png',confidence=0.8,grayscale=True)
location = pyautogui.locateCenterOnScreen('3.png',confidence=0.8,grayscale=True)
# 打印截图所在位置
print(location)
# 鼠标移动到（114，514）坐标,过程持续3秒
pyautogui.moveTo(*location, 3)
# 输出结果
# Point(x=1547, y=1563)


# def test1():
#     >> > t = locateOnScreen('images/test1.png', region=(0, 940, 1919, 939))
#     >> > print(center(t))
#
#     Point(x=873, y=1056)