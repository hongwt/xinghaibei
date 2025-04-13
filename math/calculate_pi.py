import math

def calculate_pi(n, r=1):
    """
    使用内接正多边形的周长来计算π
    :param n: 多边形的边数
    :param r: 圆的半径（默认为1）
    :return: π的近似值
    """
    a = 2 * r * math.sin(math.pi / n)
    P_inner = n * a
    pi_approx = P_inner / (2 * r)
    return pi_approx

# 示例：使用内接正1000边形来计算π
n = 1000000000000
pi_approx = calculate_pi(n)
print(f"使用内接正{n}边形计算的π的近似值是: {pi_approx}")