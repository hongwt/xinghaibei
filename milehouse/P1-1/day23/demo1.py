import random
num = random.randint(1, 100)
print(num)
while True:
    nums=int(input("请输入一个1-100的数字:"))
    if nums>num:
        print("猜大了")
    elif nums<num:
        print("猜小了")
    else:
        print("猜对了")
        