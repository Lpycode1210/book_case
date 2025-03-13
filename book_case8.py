#输入数值计算平均数，中位数，标准差
from math import sqrt
def getnum():
    nums=[]
    inumstr=input("输入数字（空按回车推出):")
    while inumstr !="":
        nums.append(eval(inumstr))
        inumstr=input("输入数字（空按回车推出):")
    return nums
def mean(numbers):
    s=0.0
    for num in numbers:
        s=s+num
    return s/len(numbers)
def dev(numbers,mean):#标准差
    sdev=0.0
    for num in numbers:
        sdev = sdev + (num-mean)**2
    return sqrt(sdev/(len(numbers)-1))#sqrt 计算平方根
def median(numbers):#中位数
    new = sorted(numbers)#生成一个新的排序后的列表，默认从小到大
    size = len(numbers)
    if size%2==0:#整除2余数0
        med = (new[size//2-1]+new[size//2])/2
    else:
        med = new[size//2]
    return med
n=getnum()
m=mean(n)
print("平均值:{}，标准差:{},中位数:{}".format(m,dev(n,m),median(n)))


