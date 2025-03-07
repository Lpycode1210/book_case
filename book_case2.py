# import turtle #图形绘制函数库  面向对象，引用里面的函数
# turtle.setup(650,350,200,200)#尺寸（width,height,startx,starty）后两个表示在我屏幕上出现的位置
# turtle.penup()# 提起画笔，移动到起始位置
# turtle.fd(-250)# 向前移动到画图起始点,窗口中间位置为（0，0）
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor("purple")
# turtle.seth(-40)#设置初始方向为-40度
# for i in range(4):#循环四次
#     turtle.circle(40,80)#半径为40的圆弧，角度为80度
#     turtle.circle(-40,80)
# #turtle.circle(40,80/2)#调整位置到水平方向
# turtle.fd(40)
# turtle.circle(16,180)
# turtle.fd(40*2/3)



#or from (库) import 函数
from turtle import * #引入里面的全部函数
setup(650,350,200,200)#尺寸
penup()# 提起画笔，移动到起始位置
fd(-250)# 向前移动到画图起始点
pendown()
pensize(25)
pencolor("pink")
seth(-40)#设置初始方向为-40度
for i in range(4):#循环四次
    circle(40,80)#半径为40的圆弧，角度为80度
    circle(-40,80)
circle(40,80/2)#调整位置到水平方向
fd(40)
circle(16,180)
fd(40*2/3)