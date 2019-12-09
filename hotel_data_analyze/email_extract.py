import pandas as pd

i=0
chunksize=10**6
for data in pd.read_csv(r'E:\data\kf1.csv',names=['name','tp','id','gender',
                                                  'birthday','add','mobile','tel','email'],chunksize=chunksize):
    #print(data['id'])

    data1=data[['email']]
    data1.to_csv(r'E:\data\kf_email.txt',sep=' ',mode='a+',encoding='utf-8')
    i += 1
    print(i*chunksize)