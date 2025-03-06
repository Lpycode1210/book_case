#1
# TempStr = input("please input temperature value with symbol:")
# if TempStr[-1] in ['F','f']:      #表示访问字符串的最后一个字符
#     C = (eval(TempStr[0:-1])-32)/1.8#eval 将输入的字符串转变成python语句，并执行。
#     #[0:-1]表示从字符串的第0个字符开始，一直到倒数第1个字符，它会去掉字符串的最后一个字符
#     print("The temperature after conversion is{:.2f}C".format(C))#保留c两位小数
# elif TempStr[-1] in ['C','c']:
#     F=1.8*eval(TempStr[:-1])+ 32
#     print("The temperature after conversion is{:.2f}F".format(F))
# else:
#     print("input error")

#2
# TempStr=input("please input temperature value with symbol:")
# while TempStr[-1] not in ["N","n"]:#不是N，n 时执行，如果输入N or n 就会退出程序
#     if TempStr[-1] in ['F','f']:
#         C = (eval(TempStr[0:-1])-32)/1.8
#         print("The temperature after conversion is{:.2f}C".format(C))
#     elif TempStr[-1] in ['C','c']:
#         F = 1.8 * eval(TempStr[:-1]) + 32
#         print("The temperature after conversion is{:.2f}F".format(F))
#     else:
#         print("input error")
#     TempStr = input("please input temperature value with symbol:")


#3
#先定义一个函数，然后再引用
def tempconvert(valuestr):#valuestr是函数的参数，表示传递给函数的输入值
    if valuestr[-1] in ["f","F"]:
        C = (eval(valuestr[0:-1]) - 32) / 1.8
        print("The temperature after conversion is{:.2f}C".format(C))
    elif valuestr[-1] in ['C','c']:
        F = 1.8 * eval(valuestr[:-1]) + 32
        print("The temperature after conversion is{:.2f}F".format(F))
    else:
        print("input error")
TempStr = input("please input temperature value with symbol:")
tempconvert(TempStr)#quote



