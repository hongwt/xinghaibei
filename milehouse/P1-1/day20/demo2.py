while True:
    a=float(input("请输入你的成绩:"))
    if a<60:
        print("你的成绩是：%d,  成绩没有合格, 你需要努力了!" %a)
    elif a>=60 and a<80:
        print("你的成绩是：%d, 成绩合格, 希望继续努力!" %a)
    elif a>=80 and a<100:
        print("你的成绩是：%d, 成绩优秀, 继续保持!" %a)
    elif a==100:
        print("你的成绩是：%d, 好好好!!!" %a)
    else:
        print("你的成绩是：%d, 成绩不合法, 请重新输入!" %a)

