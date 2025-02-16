while True:
    a=str(input("今天周几："))
    if(a=="周一"or a=="周三" or a=="周五"):
        print("今天是篮球课")
    elif(a=="周二"or a=="周四" or a=="周六"):
        print("编程课")
    elif(a=="周日"):
        print("书法课")
    else:
        print("输入有误")
