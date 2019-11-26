# python if 逻辑判断
x = "abcde"
# 判断包含关系 if
if 'b' in x:
    print("b 包含在 x字符串序列中")
#  elif
if 'bb' in x:
    print("bb 包含在 x字符串序列中")
elif 'c' in x:
    print("c 包含在 x字符串序列中")
# else
if 'bb' in x:
    print("bb 包含在 x字符串序列中")
elif 'cc' in x:
    print("cc 包含在 x字符串序列中")
else:
    print("bb cc 均不包含在 x字符串序列中")
