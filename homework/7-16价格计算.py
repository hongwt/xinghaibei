while True:
    a=float(input("请输入商品价格(元)："))
    if(a<=10):
        print(f"享受折扣0.1折,应付{a * 0.1:.2f} 元")   
    else:
        print(f"享受折扣0.2折,应付{a * 0.2:.2f}元")
    
