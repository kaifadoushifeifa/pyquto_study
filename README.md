# pyquto_study

##常见的一些操作
moveTo（x，y）                将鼠标移动到指定的 x、y 坐标   （屏幕以左上角为原点（0,0），向下y增加，向右x增加）

moveTo（x，y,duration）  使用duration值设置几秒后移动鼠标到指定的 x、y 坐标

moveRel （x，y）             相对于当前的鼠标位置移动鼠标。

size()                                  获得屏幕的width和height值

position()                            获得当前鼠标的位置

locateOnScreen(' *.png')   在屏幕上通过图像识别找到与图像相同的位置，并返回坐标size

center(size)                       可通过locateOnScreen获得的图像坐标对象，并返回其图像上的 中心点坐标（可用moveTo,移动到此处）

dragTo（x，y）                 按下左键移动鼠标。

dragRel （x，y）              按下左键，相对于当前位置移动鼠标。

click（x，y，button）       模拟点击（默认是左键）。

rightClick()                         模拟右键点击。

middleClick()                     模拟中键点击。

doubleClick()                     模拟左键双击。

mouseDown（x，y，button）模拟在 x、y 处按下指定鼠标按键。

mouseUp（x，y，button）模拟在 x、y 处释放指定键。

scroll （units）                  模拟滚动滚轮。正参数表示向上滚动，负参数表示向下滚动。

typewrite（message）      键入给定消息字符串中的字符。

typewrite（[key1，key2]）键入给定键字符串，只能是英文。

press（key）                     按下并释放给定键。

keyDown（key）               模拟按下给定键，不释放。

keyUp（key）                   模拟释放给定键。

hotkey（[key1，key2]）   模拟按顺序按下给定键字符串，然后以相反的顺序释放，（实现粘贴复制操作）

pyautogui.PAUSE=1　　  将pyautogui.PAUSE 设置为 1，即每次函数调用后暂停一秒。

pyautogui.FAILSAFE=True  启动自动防故障功能

##我肯定要封装一下