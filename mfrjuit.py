a=int(input("长(厘米):"))
b=int(input("宽(厘米):"))
h=int(input("高(厘米):"))
体积=a*b*h
体积转化=体积/1000000
print(format(float(体积转化), ".2f"),"立方米")

