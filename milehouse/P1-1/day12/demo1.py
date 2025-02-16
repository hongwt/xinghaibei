def add(a, b):
    return a + b

def main():
    try:
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        result = add(num1, num2)
        print(f"结果是: {result}")
    except ValueError:
        print("请输入有效的数字")

if __name__ == "__main__":
    main()