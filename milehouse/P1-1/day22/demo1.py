name=str(input("请输入名字："))
test=int(input("请输入数字1和数字2，数字1代表不出门，数字2代表出门:"))
if test=='2':
    money=int(input("请输%s上的钱数:"%name))
    print("%s正在赶往商店"%name)
    print("%s到达商店"%name)
    if money>=1:
        print("%s身上的钱为%d可以买糖果"%(name,money))
    else:
        print("%s身上的钱不够或者没带钱,无法购买糖果"%name)
else:
    print("%s没有出门"%name)
    