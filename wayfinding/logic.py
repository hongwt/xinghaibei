# 逻辑模块：处理查找和路径算法
import collections

def find_student(name, students_data):
    """
    查找学生
    返回: 列表，包含该学生的所有信息
    """
    return students_data.get(name, [])

def find_path(start_node, end_node, graph):
    """
    使用 BFS (广度优先搜索) 寻找最短路径
    """
    if start_node not in graph or end_node not in graph:
        return None
    
    queue = collections.deque([[start_node]])
    visited = set([start_node])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == end_node:
            return path
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
    return None
