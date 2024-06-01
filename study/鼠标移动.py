# 导入库
import time
import pyautogui
#鼠标移动
def  test():
    # 等待一会方便观察，随后鼠标移动到x:114,y:514的位置
    time.sleep(2)
    pyautogui.moveTo(114, 514)
    # 等待一会方便观察，随后鼠标移动到x不变(114),y:191的位置
    time.sleep(2)
    pyautogui.moveTo(None, 191)
    # 等待一会方便观察，随后鼠标移动到x:981,y不变(191)的位置
    time.sleep(2)
    pyautogui.moveTo(981, None)
#鼠标移动耗时
def test1():
    # 鼠标移动到（114，514）坐标,过程持续3秒
    pyautogui.moveTo(114, 514, 3)
#鼠标在当前位置按住鼠标左键并移动至
def test2():
    # 将鼠标在当前位置按住鼠标左键并移动至（300，400）坐标
    pyautogui.dragTo(100, 200,duration = 3, button='left')

def test3():

    # 在（114，514）坐标单击鼠标左键
    pyautogui.click(114, 514, button='left')

def test4():

    # 在当前位置向上滚动10单位量
    pyautogui.scroll(10)
    # 在(114,514)坐标向下滚动10单位量
    pyautogui.scroll(114, 514, -10)
def test5():
    #移动速度渐变
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)  # 开始很慢，不断加速
    pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)  # 开始很快，不断减速
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # 开始和结束都快，中间比较慢
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)  # 一步一徘徊前进
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # 徘徊幅度更大，甚至超过起点和终点


if __name__ == '__main__':
    test4()