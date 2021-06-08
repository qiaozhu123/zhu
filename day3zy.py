#n=1
#sum=0
#while n<=10:
#    a=int(input("输入%d个数字:"%n))
#   n=n+1
#   sum=sum+a
#print("总数为：",sum)


#n=1
#sum=0
#max=0
#while n<=10:
    #a = int(input("输入%d个数字:"%n))
    #n=n+1
    #sum=sum+a
    #if max<=a:
     #max=a
     #print("输出最大值：",max)
     #print("总数为：",sum)
     #print("平均值为：",sum/10)


#import random
#num=random.randint(50,150)
#print(num)


# a=int(input ("请输入边长a:"))
# b=int(input ("请输入边长b:"))
# c=int(input ("请输入边长c:"))
# if a+b>c and a+c>b and b+c>a:
#   if a==b and a==c:
#    print("等边三角形")
#   elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
#    print("直角三角形")
#   elif a==b or a==c or b==c:
#    print("等腰三角形")
#   else:
#    print("构成普通三角形")
# else:
#     print("不构成三角形")


# A=56
# B=78
# A=A+B
# B=A-B
# A=A-B
# print("A=",A)
# print("B=",B)


# name = "root"
# password = "admin"
# n = 3
# while True:
#     name1 = input("用户名：")
#     password1 = input("密码：")
#     if  name1 == name and password1 == password:
#         print("登陆成功")
#         break
#     else:
#         print("登录失败")
#         n = n - 1
#     if n == 0:
#             print("系统锁定")
#             break

# i=1
# sum=0
# while i<101:
#     sum=sum+i
#     i=i+1
# print("总数为：",sum)


# d=1
# b=0
# while True:
#     b=b+3
#     if b>=20:
#         break
#     b=b-2
#     d=d+1
# print("第",d,"天可以出来")


# names=["北京","上海","广东"]
# names.extend(["哈尔滨","长春","沈阳","南京","济南","合肥","石家庄","郑州","武汉",
# "长沙","南昌","西安","太原","成都","西宁","海口","广州","贵阳","杭州","福州","台北","兰州","昆明"])
# print(names)
# names[1]=("广东")
# names[2]=("上海")
# print(names)
# gdp=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# sum=0
# a=0
# while a<=7:
#     sum=sum+gdp[a]
#     a=a+1
# print("gdp的总和为：",sum)
# print("gdp的平均值：",sum/8)


a = [1,5,21,30,15,9,30,24]
sum=0
i=0
while i<=7:
    if a[i]%5 == 0:
        sum=sum+a[i]
    i=i+1
print("和为:",sum)

















