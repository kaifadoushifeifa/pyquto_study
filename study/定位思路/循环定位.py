from pyautogui import *
'''
        可以对一个icon截多张不同的图，每一张图都代表这个icon，只要定位其中一张图就能定位这个icon。

        对locateOnScreent()函数进行二次封装，多张图片之间用 ' | ' 间隔，实现循环找图
'''

# 把字符串按'|'切割
def word_cut(args):
    tup = []
    if '|' in args:
        re1 = args.split('|')
        return re1
    else:
        tup.append(args)
        return tuple(tup)


# 判断图像是否找到，如果找到就返回True，没找到就跳过
def assertPIC(args):
    if locateOnScreen(args) == None:
        pass
    else:
        return True


# 循环找图，找到就返回图像中心点，没找到就打印'没找到'
def img_locat(args):
    arg = word_cut(args)
    for i in range(len(arg)):
        if assertPIC(arg[i]):
            return center(locateOnScreen(arg[i]))
        else:
            print('没找到')


# 测试
print(img_locat('images/test.png|images/test1.png'))