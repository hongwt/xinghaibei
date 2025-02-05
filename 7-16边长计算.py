while True:
    a=input("是正方形还是长方形:")
    if (a=="长方形"):
        b=float(input("长是:"))
        c=float(input("宽是:"))
        print("周长是",(b+c)*2)
    else:
        d=float(input("请输入边长:"))
        print("周长是",d*4)
