import pandas as pd
import datetime
import matplotlib.pyplot as plt

starttime=datetime.datetime.now()
#总数统计
allcount = 0
# 性别统计
sexcount = 0
# 男女统计
malecount = 0
femalecount = 0
unknowcount = 0

#块大小
chunksize= 10**6
for data in pd.read_csv(r'E:\data\kf1.csv',names=['name','tp','id','gender','birthday','add','mobile','tel','email'],chunksize=chunksize):
    print('---------------------------')
    datacount=data.count()
    #print(datacount)
    #总数统计
    allcount = allcount + datacount['name']
    #性别统计
    sexcount = sexcount + datacount['gender']
    print('统计数量%d'%sexcount)
    gendercount = data['id'].groupby(data['gender'])#按照性别对ID进行分组
    #print(gendercount.count())#统计每个性别有多少id
    malecount= malecount + gendercount.count()['M']
    print('男性数量%d'%malecount)
    femalecount = femalecount + gendercount.count()['F']
    print('女性数量%d'%femalecount)
    unknowcount= (sexcount - malecount - femalecount) - unknowcount
    print('未知数量%d'%unknowcount)
    endtime=datetime.datetime.now()
    print(endtime - starttime)

totalendtime=datetime.datetime.now()
print(totalendtime - starttime)
print('统计总数%d'%sexcount,'男性总数%d'%malecount,'女性总数%d'%femalecount,'性别未知%d'%unknowcount)


plt.rcParams['font.sans-serif']=['SimHei']
quants=[]
quants.append(malecount)
quants.append(femalecount)
quants.append(unknowcount)

plt.figure(figsize=(6,6))
labels=['男性','女性','未知']
sizes=[malecount,femalecount,unknowcount]
explode=(0,0,0)#将某一块分割出来，值越大分割出的间歇越大
plt.pie(sizes,
        explode=explode,
        labels=labels,
        labeldistance=1.2,#图例距离圆心半径倍距离
        autopct='%3.2f%%',#数值保留固定小数位
        shadow=True,#无阴影设置
        startangle=90,#逆时针起始角度设置
        pctdistance=0.6#数值距离圆心半径倍距离
        )
#plt.title('男女比例分布')
plt.axis('equal')
plt.legend()
plt.show()
#plt.savefig('gender.png')





























