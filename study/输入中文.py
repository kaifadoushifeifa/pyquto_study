import time
import pyautogui
import pyperclip

# 将中文复制到剪贴板
pyperclip.copy("你\n好")

time.sleep(2)
# 模拟按下Ctrl+V粘贴
pyautogui.hotkey('Ctrl', 'V')

# 回车
pyautogui.typewrite("\n", interval=2)
# 回车的另一种方法
# pyautogui.hotkey('enter')
