import random 

num = random.randint(1, 50)
while True:
    computer = int(input('请输入一个数字:'))
    if computer > num:
        print('大了')
    elif computer < num:
        print('小了')
    else:
        print('猜对了')
        break
print('电脑数字是:', num)