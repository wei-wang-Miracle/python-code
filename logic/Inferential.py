# 列表以及字典推导式
# 列表正常写法
list = []
for i in range(1, 11):
    if i % 2 == 0:
        list.append(i)
print(list)
# 推导式写法  renturn method  condition
list.clear()
list = [i for i in range(1, 11) if (i % 2) == 0]
print(list)
list = [i + i for i in range(1, 11) if (i % 2) == 0]
print(list)
# 字典正常写法
map = {}
for i in range(1, 11):
    if i % 2 == 0:
        map[i] = i * i
print(map)
# 推导式写法  renturn method  condition
map = {i: i + i for i in range(1, 11) if i % 2 == 0}
print(map)
