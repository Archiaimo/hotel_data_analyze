import pandas as pd
import datetime
import matplotlib.pyplot as plt

starttime=datetime.datetime.now()
chunksize = 10**5
monthlist=['01','02','03','04','05','06','07','08','09','10','11','12']
monthnamelist=['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月']
monthallseries = pd.Series([0,0,0,0,0,0,0,0,0,0,0,0])
monthallseries.index = monthlist
#print(proallseries)

i = 0
for data in pd.read_csv(r'E:\data\kf1.csv',names=['name','tp','id','gender','birthday','add','mobile','tel','email'],chunksize=chunksize):
    #print(data)
    #筛选数据集，条件为tp列为ID，id列字符串化，前两位在prolist列表中
    month=data[(data['tp'] == 'ID') & (data['birthday'].astype(str).str[4:6].isin(monthlist))]
    monthseries=month['id'].groupby(month['birthday'].astype(str).str[4:6]).count()
    print('----------start-------------')
    monthallseries = monthallseries.add(monthseries)
    print(monthallseries)
    endtime=datetime.datetime.now()
    i += 1
    print(endtime-starttime)
    print(chunksize * i)

totaltime = datetime.datetime.now()
print(totaltime-starttime)

plt.rcParams['font.sans-serif']=['SimHei']
monthallseries.index=monthnamelist
monthallseries=monthallseries.sort_values(ascending=True)
print(monthallseries)
monthallseries.plot.barh()
plt.title('生日月份分布图')
plt.show()