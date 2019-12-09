import pandas as pd
import datetime
import matplotlib.pyplot as plt
from phone import Phone
phonenum = '13085655212'
info =Phone().find(phonenum)
starttime = datetime.datetime.now()
chunksize = 10 ** 5
phonedict = {"联通":0, "移动":0, "电信":0}
i = 0
# 联通
unicomList = ['130', '131', '132', '145', '155', '156', '166', '171', '175', '176', '185', '186']
# 移动
mobileList = ['134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '157', '158',
              '159', '172', '178','182', '183', '184', '187', '188', '198']
# 电信
telecomList = ['133', '149', '153', '173', '177', '180', '189', '181', '191', '199']
cellphoneList = ['130', '131', '132', '145', '155', '156', '166', '171', '175', '176', '185', '186', '134', '135',
                 '136', '137', '138', '139', '147', '150', '151', '152', '157', '158', '159', '172', '178', '182',
                 '183', '184', '187', '188', '198', '133', '149', '153', '173', '177', '180', '189', '181', '191',
                 '199']
for data in pd.read_csv(r'E:\data\kf1.csv', names=['name', 'tp', 'id', 'gender', 'birthday',
                                                   'add', 'mobile', 'tel', 'email'], chunksize=chunksize):
    unicomdata = data
    unicomdata['mobile']=unicomdata['mobile'].astype(str)
    unicomdata=unicomdata[unicomdata['mobile'].astype(str).str[:3].isin(unicomList)]
    phonedict['联通'] = phonedict['联通'] + unicomdata['mobile'].count()
    print(phonedict['联通'])

    mobiledata = data
    mobiledata['mobile'] = mobiledata['mobile'].astype(str)
    mobiledata = mobiledata[mobiledata['mobile'].astype(str).str[:3].isin(mobileList)]
    phonedict['移动'] = phonedict['移动'] + mobiledata['mobile'].count()
    print(phonedict['移动'])

    telecomdata = data
    telecomdata['mobile'] = telecomdata['mobile'].astype(str)
    telecomdata = telecomdata[telecomdata['mobile'].astype(str).str[:3].isin(telecomList)]
    phonedict['电信'] = phonedict['电信'] + telecomdata['mobile'].count()
    print(phonedict['电信'])

    print(phonedict)
    print('---------------------')

    endtime = datetime.datetime.now()
    i += 1
    print(endtime - starttime)
    print(chunksize * i)

totaltime = datetime.datetime.now()
print(totaltime - starttime)
series = pd.Series(phonedict, index=phonedict.keys())
print(series)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(6, 6))  # 调节图形大小
labels = ['联通', '移动', '电信']  # 定义标签
explode = (0, 0, 0)  # 将某一块分割出来，值越大分割出的间隙越大
plt.pie(phonedict.values(),
        explode=explode,
        labels=labels,
        labeldistance=1.2,  # 图例距圆心半径倍距离
        autopct='%3.2f%%',  # 数值保留固定小数位
        shadow=True,  # 无阴影设置
        startangle=180,  # 逆时针起始角度设置
        pctdistance=0.6)  # 数值距圆心半径倍数距离
plt.axis('equal')
plt.legend()
plt.title('手机运营商分布图')
plt.show()
