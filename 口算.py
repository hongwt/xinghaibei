import random

def generate_arithmetic_problems(num_rows, num_cols):
    problems = []
    for _ in range(num_rows):
        row_problems = []
        for _ in range(num_cols):
            # 生成两个两位数
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            
            # 随机选择乘法或除法
            if random.choice([True, False]):
                # 乘法
                result = num1 * num2
                problem = f"{num1} * {num2} = "
                row_problems.append(problem)
            else:
                # 除法，确保除数不为0
                while num2 == 0:
                    num2 = random.randint(10, 99)
                if num1 % num2 == 0:  # 确保结果为整数
                    result = num1 // num2
                    problem = f"{num1} / {num2} = "
                    row_problems.append(problem)
        problems.append(row_problems)
    
    return problems

# 生成25行，每行4个口算题目
problems = generate_arithmetic_problems(25, 4)

# 打印题目
for row in problems:
    for problem in row:
        print(problem, end='   ')
    print()
    
    
