a=input("是不是长方形:");
if not (a=="是"):
    print("不是长方形不进行计算。");
else:
    b=int(input("请输入长方形的长:"));
    c=int(input("请输入长方形的宽:"));
    d=(b+c)*2;
    print("长方形的周长是",d);
