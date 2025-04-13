import numpy as np
import matplotlib.pyplot as plt

def draw_polygon_and_circle(n, r=1):
    """
    绘制圆以及内接和外接的正多边形，并计算π的近似值
    :param n: 多边形的边数
    :param r: 圆的半径（默认为1）
    """
    # 创建角度数组
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)

    # 计算内接多边形的顶点坐标
    inner_x = r * np.cos(angles)
    inner_y = r * np.sin(angles)

    # 计算外接多边形的顶点坐标
    outer_x = r / np.cos(np.pi / n) * np.cos(angles)
    outer_y = r / np.cos(np.pi / n) * np.sin(angles)

    # 闭合多边形
    inner_x = np.append(inner_x, inner_x[0])
    inner_y = np.append(inner_y, inner_y[0])
    outer_x = np.append(outer_x, outer_x[0])
    outer_y = np.append(outer_y, outer_y[0])

    # 绘制圆
    circle = plt.Circle((0, 0), r, color='blue', fill=False, label='Circle')
    fig, ax = plt.subplots()
    ax.add_patch(circle)

    # 绘制圆的直径
    ax.plot([-r, r], [0, 0], 'b--', label='Diameter')
    ax.plot([0, 0], [-r, r], 'b--')

    # 绘制内接多边形
    ax.plot(inner_x, inner_y, 'r--', label=f'Inscribed {n}-gon')

    # 绘制外接多边形
    ax.plot(outer_x, outer_y, 'g--', label=f'Circumscribed {n}-gon')

    # 设置图形属性
    ax.set_aspect('equal')
    ax.legend()
    plt.show()

    # 计算π的近似值
    pi_inner = n * 2 * r * np.sin(np.pi / n) / (2 * r)
    pi_outer = n * 2 * r * np.tan(np.pi / n) / (2 * r)
    print(f"使用内接{n}-边形计算的π的近似值是: {pi_inner}")
    print(f"使用外接{n}-边形计算的π的近似值是: {pi_outer}")

# 示例：绘制一个圆以及内接和外接的正12边形
draw_polygon_and_circle(96)