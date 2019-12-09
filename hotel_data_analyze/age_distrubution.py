import pandas as pd
import datetime
import matplotlib.pyplot as plt

starttime=datetime.datetime.now()
chunksize = 10**5
agelist=['193','194','195','196','197','198','199','200']
agenamelist=['30后','40后','50后','60后','70后','80后','90后','00后']
ageallseries = pd.Series([0,0,0,0,0,0,0,0])
ageallseries.index = agelist
#print(proallseries)

i = 0
for data in pd.read_csv(r'E:\data\kf1.csv',names=['name','tp','id','gender','birthday','add','mobile','tel','email'],chunksize=chunksize):
    #print(data)
    #筛选数据集，条件为tp列为ID，id列字符串化，前两位在prolist列表中
    age=data[(data['tp'] == 'ID') & (data['birthday'].astype(str).str[:3].isin(agelist))]
    ageseries=age['id'].groupby(age['birthday'].astype(str).str[:3]).count()
    print('----------start-------------')
    ageallseries = ageallseries.add(ageseries)
    print(ageallseries)
    endtime=datetime.datetime.now()
    i += 1
    print(endtime-starttime)
    print(chunksize * i)

totaltime = datetime.datetime.now()
print(totaltime-starttime)
plt.rcParams['font.sans-serif']=['SimHei']
ageallseries.index=agenamelist
ageallseries=ageallseries.sort_values(ascending=True)
print(ageallseries)
ageallseries.plot.barh()
plt.title('年龄分布图')
plt.show()