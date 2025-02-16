while True:
    score=int(input("分数:"))
    if (90<=score<=100):
        print("优秀")
    elif (80<=score<=90):
        print("良好")
    elif (70<=score<=80):
        print("一般")    
    elif (60<=score<=70):
        print("及格")
    elif (0<=score<60):
        print("不及格") 
    else:
        print("输入错误")
