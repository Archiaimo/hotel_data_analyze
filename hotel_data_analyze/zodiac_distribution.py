import pandas as pd
import datetime
import matplotlib.pyplot as plt
# 获得生肖函数
def get_zodiac(year):
    zodiac = ("猴", "鸡", "狗","猪", "鼠", "牛", "虎", "兔", "龙", "蛇", "马","羊")
    return zodiac[year % 12]

starttime = datetime.datetime.now()
chunksize = 10 ** 5
zodiacdict = {"鼠":0, "牛":0, "虎":0, "兔":0, "龙":0, "蛇":0, "马":0,
              "羊":0, "猴":0, "鸡":0, "狗":0, "猪":0}
print(zodiacdict)
i = 0
agelist = ['193', '194', '195', '196', '197', '198', '199', '200']
for data in pd.read_csv(r'E:\data\kf1.csv', names=['name', 'tp', 'id', 'gender', 'birthday',
                                                   'add', 'mobile', 'tel', 'email'], chunksize=chunksize):
    yeardata = data[(data['tp'] == 'ID') & (data['birthday'].astype(str).str[:3].isin(agelist))]
    print('--------start------------')
    years = yeardata.birthday.values
    for index in years:
        date = index
        year = int(str(date)[:4])
        name = get_zodiac(year)
        zodiacdict[name] = zodiacdict[name] + 1
    endtime = datetime.datetime.now()
    i += 1
    print(endtime - starttime)
    print(chunksize * i)
    print(zodiacdict)
totaltime = datetime.datetime.now()
print(totaltime - starttime)
series = pd.Series(zodiacdict, index=zodiacdict.keys())
plt.rcParams['font.sans-serif'] = ['SimHei']
series = series.sort_values(ascending=False)
print(series)
series.plot.bar()
plt.title('生肖分布图')
plt.show()




