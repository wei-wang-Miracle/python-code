# python for 循环
zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
for x in zodiac:
    if "鸡" == x:
        print(x)
    elif "猪" == x:
        print(str(2019) + ": " + x)
    else:
        print("else:" + x)
# 1到100循环相加
sum = 0
# range(1, 101) 包前不包后
for i in range(1, 101):
    sum += i
print(sum)
# 循环年份 获取生肖  并完成字符串替换
for year in range(2000, 2020):
    print("%s 年的生肖是: %s" % (year, zodiac[year % 12 - 4]))
