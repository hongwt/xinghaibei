a=input("是不是正方形:")
if not(a=="是"):
    print("不是正方形,不需要计算")
else:
    print("是正方形")
    a=int(input("请输入边长:"))
    print("周长是",a*4)
