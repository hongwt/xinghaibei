a_person = {'name': 'xiaoming', 'age': 17, 'height': '170cm'}
print(a_person.keys())  # dict_keys(['name', 'age', 'height'])
a_person.pop('age')  # 删除键为'age'的键值对
print(a_person)  # {'name': 'xiaoming', 'height': '170cm'}