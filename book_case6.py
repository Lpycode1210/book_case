import turtle,datetime
# def drawline(draw):
#     turtle.pendown() if draw else turtle.penup()#根据draw布尔值决定执行down or up
#     turtle.fd(40)
#     turtle.right(90)
# def drawdigit(d):
#     drawline(True) if d in [2, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
#     drawline(True) if d in [0,1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
#     drawline(True) if d in [0,2, 3, 5, 6, 8, 9] else drawline(False)
#     drawline(True) if d in [0,2, 6, 8, ] else drawline(False)
#     turtle.left(90)
#     drawline(True) if d in [0, 4 ,5, 6,8,9 ] else drawline(False)
#     drawline(True) if d in [0,2,3,5,6,7,8,9] else drawline(False)
#     drawline(True) if d in [0, 1,2,3,4,7,8,9] else drawline(False)
#     turtle.left(180)
#     turtle.penup()
#     turtle.fd(20)
# def drawdata(data):
#     for i in data:
#         drawdigit(eval(i))#eval 是一个Python内置函数，它将字符串作为表达式进行求值，并返回结果
# def main():
#     turtle.setup(800,350,200,200)
#     turtle.penup()
#     turtle.fd(-300)
#     turtle.pensize(5)
#     drawdata(datetime.datetime.now().strftime('%Y%m%d'))
#     turtle.hideturtle()
# main()
# #turtle.write('年'，font=("Arial",18,"normal")) 字体样式
print((datetime.datetime.now().strftime('%Y%m%d')))