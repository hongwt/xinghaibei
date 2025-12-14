import unittest
import logic
import data

class TestWayfinding(unittest.TestCase):
    def test_find_student(self):
        # 测试查找存在的学生
        results = logic.find_student("张小明", data.STUDENTS)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['grade'], 5)
        
        # 测试查找重名学生
        results = logic.find_student("李华", data.STUDENTS)
        self.assertEqual(len(results), 2)
        
        # 测试查找不存在的学生
        results = logic.find_student("孙悟空", data.STUDENTS)
        self.assertEqual(len(results), 0)

    def test_find_path(self):
        # 测试存在的路径
        path = logic.find_path("校门口", "1-1", data.MAP_GRAPH)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "校门口")
        self.assertEqual(path[-1], "1-1")
        # 验证路径连通性
        for i in range(len(path)-1):
            self.assertIn(path[i+1], data.MAP_GRAPH[path[i]])
            
        # 测试不存在的节点
        path = logic.find_path("校门口", "火星", data.MAP_GRAPH)
        self.assertIsNone(path)

if __name__ == '__main__':
    unittest.main()
