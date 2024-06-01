# 导入库
import pyautogui

def test1():
    # 模拟键盘输入Hello world
    pyautogui.write('Hello world!')

def test2():
    # 模拟键盘输入Hello world,输入两个字符之间的间隔为0.25秒
    pyautogui.write('Hello world!', interval=0.25)

def test3():
    # 模拟键盘输入H
    pyautogui.press('H')
    # 模拟键盘输入热键Enter
    pyautogui.press('Enter')

def test4():pass
if __name__ == '__main__':
    test3()