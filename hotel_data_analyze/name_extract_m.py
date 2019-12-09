import pandas as pd
import datetime
import matplotlib.pyplot as plt

starttime=datetime.datetime.now()
i = 0
chunksize= 10**5
for data in pd.read_csv(r'E:\data\kf2.csv',names=['name','tp','id','gender',
                                        'birthday','add','mobile','tel','email'],chunksize=chunksize):
    print('----------------')
    sexdata=data[(data['tp']=='ID') & (data['gender'] == 'M')]
    #print(sexdata[['name','gender']])
    name=sexdata.name.values
    #print(name)
    #print(type(name))
    with open(r'E:\data\lastname.txt','a+',errors='ignore') as f:
        for index in name:
            lastname = str(index).strip()[-1:-2:-1]
            f.write(lastname + '\t')

    i += 1
    print(i * chunksize)