import pandas as pd
import datetime
import matplotlib.pyplot as plt

starttime=datetime.datetime.now()
allcount=0
chunksize = 10**5
prolist=['11','12','13','14','15','21','22','23','31','32','33','34','35','36','37',
          '41','42','43','44','45','46','50','51','52','53','54','61','62','63','64','65']
pronamelist=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江',
             '安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川',
             '贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
proallseries = pd.Series([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
proallseries.index = prolist
i = 0
for data in pd.read_csv(r'E:\data\kf1.csv',names=['name','tp','id','gender','birthday','add','mobile','tel','email'],chunksize=chunksize):
    #print(data)
    #筛选数据集，条件为tp列为ID，id列字符串化，前两位在prolist列表中
    pro=data[(data['tp'] == 'ID') & (data['id'].str[:2].isin(prolist))]
    proseries=pro['name'].groupby(pro['id'].str[:2]).count()
    print('----------start-------------')
    #print(proseries)
    proallseries = proallseries.add(proseries)
    #print(proallseries)
    endtime=datetime.datetime.now()
    i += 1
    print(endtime-starttime)
    print(chunksize * i)

totaltime = datetime.datetime.now()
print(totaltime-starttime)
plt.rcParams['font.sans-serif']=['SimHei']
proallseries.index=pronamelist
proallseries=proallseries.sort_values(ascending=True)
print(proallseries)
proallseries.plot.barh()
plt.title('省份人口分布图')
plt.show()