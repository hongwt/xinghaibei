score=int(input("请输入你的分数:"))
if score>=10 and score<50:
    print("白银")
elif score>=50 and score<80:
    print("黄金")
elif score>=80:
    print("王者")
else:
    print("青铜")
