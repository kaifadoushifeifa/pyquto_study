import time

import pyautogui
import pyperclip


class ZdxAutoGui:
    def __init__(self):pass
    @classmethod
    def write_ch(self,word):
        # 将中文复制到剪贴板
        pyperclip.copy(word)
        time.sleep(1)
        # 模拟按下Ctrl+V粘贴
        pyautogui.hotkey('Ctrl', 'V')
    @classmethod
    def enter(cls):
        pyautogui.press('Enter')