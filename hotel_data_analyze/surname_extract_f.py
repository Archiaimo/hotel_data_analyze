import pandas as pd
import datetime
import matplotlib.pyplot as plt

starttime=datetime.datetime.now()
i = 0
chunksize= 10**5
for data in pd.read_csv(r'E:\data\kf1.csv',names=['name','tp','id','gender',
                                        'birthday','add','mobile','tel','email'],chunksize=chunksize):
    print('----------------')
    sexdata=data[(data['tp']=='ID') & (data['gender'] == 'F')]
    #print(sexdata[['name','gender']])
    name=sexdata.name.values
    #print(name)
    #print(type(name))
    with open(r'E:\data\xing-f.txt','a+',errors='ignore') as f:
        for index in name:
            firstname = str(index)[:1]
            f.write(firstname + '\t')

    i += 1
    print(i * chunksize)