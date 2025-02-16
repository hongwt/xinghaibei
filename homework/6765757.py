
while True:
    score = float(input("你的分数是:"))
    if score >= 100:
        print("任选豪华套餐")
    elif 95<=score <100:
        print("吃一顿肯德基")
    elif score < 60:
        print("准备吃棍子炒肉")
    else:
        print("好好复习")         
         
    
