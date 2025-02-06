import random
secret=random.randint(1,10)
print("猜猜我心里想的数字是多少")
guess=0
time=3
while(guess!=secret)and(time>0):
        temp=input()
        guess=int(temp)
        time=time-1
        if  guess==secret:
              print("这么难的数字你都猜到了")
        else:
               if guess>secret:
                     print("大了大了")
              else:
                      print("小了小了")
                if  time>0:
                     print("再猜一次吧")
                else:
                    print("机会用完了")
print("不玩了游戏结束")
