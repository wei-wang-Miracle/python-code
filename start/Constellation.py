# 元组  根据月日 获取用户星座
# 新建星座元组数据 并指定 Unicode 字符集 防止乱码
constellation = (u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座', u'摩羯座', u'水瓶座', u'双鱼座')
# 新建星座对应的 月份日信息 进行元组嵌套  星座起始时间
monthAndDays = (
(3, 21), (4, 20), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 24), (11, 23), (12, 22), (1, 20), (2, 19))
# 用户月日
(userMonth, userDay) = (1, 26)
# 查询用户星座 用户日月 小于哪个 星座的起始日期  然后确定下标
print(constellation[len(list(filter(lambda x: x < (userMonth, userDay), monthAndDays))) - 3])
