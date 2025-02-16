name = input("请输入名字：")
test = int(input("请输入数字1和数字2，数字1代表不出门，数字2代表出门:"))

if test == 2:
    money = int(input("请输入%s上的钱数：" % name))
    print("%s正在赶往火车站" % name)
    print("%s到达火车站" % name)
    if money >= 1:
        print("%s身上的钱为%d可以买火车票" % (name, money))
        print("%s正在购买火车票" % name)
        print("%s购买火车票成功" % name)
        print("%s正在进行安检" % name)
        print("%s安检通过" % name)
        print("%s正在登录火车" % name)
        print("%s登录火车成功" % name)
    else:
        print("%s身上的钱不够或者没带钱，无法购买火车票" % name)
else:
    print("%s没有出门" % name)
