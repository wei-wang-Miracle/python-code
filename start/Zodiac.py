# 根据用户出生年来判断用户生肖
zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
# 多个序列下标 包前不包后
print(zodiac[1:4])
print(zodiac[-3])
# 问：如果我想实现输出后三位生肖应该怎么写？
print(zodiac[-3:])
# 问：字符串反向输入如何实现
print(zodiac[::-1])
# 计算生肖
year = 1993
print(zodiac[year % 12])  # 得出结论 牛， 已知1993年生肖为鸡   所以公元元年并非鼠年 而是猴年 右偏移量为8左偏移量4
# 若余数加 8 作为下标 则会出现下标溢出
# print(zodiac[2010%12 +  8])
# IndexError: string index out of range
# 选择余数 -4
print(zodiac[year % 12 - 4])
# 序列是否存在
print('猫' in zodiac)  # False
print('猫' not in zodiac)  # True
# 连接操作 +  此处不同于 java， int无法直接连接字符串
print(str(year) + ":" + zodiac[year % 12 - 4])
# 重复操作  字符串 * 重复次数
print(zodiac * 2)
# 数字则会直接得出计算结果
print(year * 2)
