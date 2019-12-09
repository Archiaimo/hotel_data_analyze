import pandas as pd

chunksize = 10**6
for data in pd.read_csv(r'E:\data\kf.csv',header=None,chunksize=chunksize):

    #print(type(data))
    data1=pd.DataFrame(data)
    #选择所需要的列
    data2=data1[[0,3,4,5,6,7,19,20,22]]

    clean1=data2.dropna(axis=1,how='all')#去除全部为nan的列
    clean2=clean1.dropna(how='all')#去除全部为nan的行

    clean2.to_csv(r'E:\data\kf1.csv',mode='a')#写入模式必须加mode，否则会被当做分隔符

