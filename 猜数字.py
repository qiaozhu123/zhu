import random
num = random.randint(0,150)
i = 0
g=5000
while i <= 15:
    number = input("请输入您要猜的数：")
    number = int(number)
    if number > num:
        g = g - 500
        print("大了！")
        print("余额为：",g)
    elif number < num:
        g = g - 500
        print("小了！")
        print("余额为：",g)
    else:
        g = g + 3000
        print("恭喜猜中！本次数字为：",num)
        print("余额为：",g)
        i= i + 1

    if g==0:
        print("系统锁定！")
        break
    if i==15:
        print("系统锁定！")
        break
