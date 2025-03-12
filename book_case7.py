#科赫曲线
import time
import turtle
start_time = time.perf_counter()
# def koch(size,n):
#     if n==0:
#         turtle.fd(size)
#     else:
#         for angle in [0,60,-120,60]:
#             turtle.left(angle)
#             koch(size/3,n-1)
# def main():
#     turtle.setup(800,400)
#     turtle.speed(0)
#     turtle.penup()
#     turtle.goto(-300,-50)
#     turtle.pendown()
#     turtle.pensize(2)
#     koch(600,5)
#     turtle.hideturtle()#只隐藏画笔的turtle形状，不影响画笔的绘制功能
# main()


def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(600,600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level=5
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.right(120)
    koch(400,level)
    turtle.hideturtle()
main()
elapsed_time = time.perf_counter() - start_time
print(f"{elapsed_time:.2f}")