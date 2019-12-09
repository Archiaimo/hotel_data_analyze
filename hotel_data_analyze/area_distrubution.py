import pandas as pd
import datetime
import matplotlib.pyplot as plt

starttime=datetime.datetime.now()
allcount=0

chunksize = 10**5
arealist=['1','2','3','4','5','6']
areanamelist=['华北','东北','华东','华中','西南','西北']
areaallseries = pd.Series([0,0,0,0,0,0])
areaallseries.index = arealist
#print(proallseries)

i = 0
for data in pd.read_csv(r'E:\data\kf1.csv',names=['name','tp','id','gender','birthday','add','mobile','tel','email'],chunksize=chunksize):
    #print(data)
    #筛选数据集，条件为tp列为ID，id列字符串化，前两位在prolist列表中
    area=data[(data['tp'] == 'ID') & (data['id'].str[:1].isin(arealist))]
    areaseries=area['name'].groupby(area['id'].str[:1]).count()
    print('----------start-------------')
    #print(proseries)
    areaallseries = areaallseries.add(areaseries)
    #print(proallseries)
    endtime=datetime.datetime.now()
    i += 1
    print(endtime-starttime)
    print(chunksize * i)

totaltime = datetime.datetime.now()
print(totaltime-starttime)
#汉化
plt.rcParams['font.sans-serif']=['SimHei']
areaallseries.index=areanamelist
areaallseries=areaallseries.sort_values(ascending=True)
print(areaallseries)
areaallseries.plot.bar()
plt.title('区域人口分布图')
plt.show()