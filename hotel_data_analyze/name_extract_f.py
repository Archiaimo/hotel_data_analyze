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
    with open(r'E:\data\lastname-f.txt','a+',errors='ignore') as f:
        for index in name:
            #print(index)
            lastname = str(index).strip()[-1:-2:-1]
            #print(lastname)
            f.write(lastname + '\t')

    i += 1
    print(i * chunksize)