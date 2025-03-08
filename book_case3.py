# import turtle
#
# # 设置画布
# turtle.setup(800, 800)
# screen = turtle.Screen()
# screen.title("正方形螺旋线")
#
# # 创建画笔
# pen = turtle.Turtle()
# pen.speed(0)  # 设置最快速度
# pen.penup()  # 抬起画笔
# pen.goto(0, 0)  # 移动到画布中心
# pen.pendown()  # 放下画笔
#
# # 初始化边长
# side_length = 10
#
# # 绘制正方形螺旋线
# while side_length <= 100:
#     for _ in range(4):
#         pen.forward(side_length)  # 绘制正方形的一边
#         pen.left(90)  # 逆时针转向
#     side_length += 5  # 增加边长
#
# # 完成绘制
# pen.hideturtle()
# turtle.done()

import turtle

# 设置画布
turtle.setup(800, 800)
screen = turtle.Screen()
screen.title("线段螺旋线")

# 创建画笔
pen = turtle.Turtle()
pen.speed(0)  # 设置最快速度
pen.penup()  # 抬起画笔
pen.goto(0, -10)  # 移动到起始位置，稍微偏下以避免从画布中心开始
pen.pendown()  # 放下画笔

# 初始化线段长度
segment_length = 10

# 绘制线段螺旋线
while segment_length <= 500:
    pen.forward(segment_length)  # 绘制线段
    pen.right(90)  # 逆时针旋转90度
    segment_length += 5  # 增加线段长度

# 完成绘制
pen.hideturtle()
turtle.done()