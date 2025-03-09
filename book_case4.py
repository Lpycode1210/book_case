# s="python"
# print("{0:*^30}".format(s))   #0可以省略
#设计进度条
# import time
# scale = 10
# print("------Start running------")
# for i in range(scale+1):
#     a,b ='**' * i,'..'*(scale-i)
#     c=(i/scale)*100
#     print("%{:^3.0f}[{}->{}]".format(c,a,b))#.0f：表示浮点数，没有小数部分
#     time.sleep(0.1)
# print("------end------")

#单行自动刷新
# import time
# for i in range(101):
#     print("\r{:3}%".format(i),end="")#\r 用于在同一行上更新输出，而不是开始新的一行.end 确保输出不会换到新的一行
#     time.sleep(0.05)
# print("\n end")


#自动刷新
import time

scale = 50
print("Start running".center(scale // 2, '-'))#居中，并用-字符填充两侧的空白。
start_time = time.perf_counter()#返回一个浮点数，表示调用时刻相对于某个特定初始点的时间，单位是秒

for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    elapsed_time = time.perf_counter() - start_time#当前时间点，减去程序开始时的时间点
    print(f"\r{c:>3.0f}%[{a}->{b}]{elapsed_time:.2f}S", end='')
    time.sleep(0.05)

print("\n" + "end".center(scale // 2, '-'))




