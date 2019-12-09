import pandas as pd
import datetime
import matplotlib.pyplot as plt
#获得星座函数
def get_constellation(month,day):
    days = (21,20,21,21,22,22,23,24,24,24,23,22)
    constellations = ("摩羯", "水瓶", "双鱼", "白羊", "金牛", "双子", "巨蟹", "狮子",
                      "处女", "天秤", "天蝎", "射手", "摩羯")
    if day < days[month-1]:
        return constellations[month - 1]
    else:
        return constellations[month]

starttime=datetime.datetime.now()
chunksize = 10**5
dictconstellation = {"摩羯":0, "水瓶":0, "双鱼":0, "白羊":0, "金牛":0, "双子":0,
                     "巨蟹":0, "狮子":0, "处女":0, "天秤":0, "天蝎":0, "射手":0}
print(dictconstellation)
i = 0
agelist = ['193', '194', '195', '196', '197', '198', '199', '200']
for data in pd.read_csv(r'E:\data\kf1.csv',names=['name','tp','id','gender','birthday',
                                                  'add','mobile','tel','email'],chunksize=chunksize):
    month_daydata=data[(data['tp'] == 'ID') & (data['birthday'].astype(str).str[:3].isin(agelist))]
    print('--------start------------')
    month_day = month_daydata.birthday.values
    try:
        for index in month_day:
            date = index
            month = int(str(date)[4:6])
            if month > 12:
                continue
            day = int(str(date)[6:8])
            if day > 31:
                continue
            name = get_constellation(month,day)
            dictconstellation[name] = dictconstellation[name] + 1
    except ValueError:
        continue
    endtime = datetime.datetime.now()
    i += 1
    print(endtime - starttime)
    print(chunksize * i)
    print(dictconstellation)
totaltime = datetime.datetime.now()
print(totaltime - starttime)
series =pd.Series(dictconstellation,index=dictconstellation.keys())
plt.rcParams['font.sans-serif']=['SimHei']
series=series.sort_values(ascending=False)
print(series)
series.plot.bar()
plt.title('星座分布图')
plt.show()
 

