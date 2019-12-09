import pandas as pd

i=0
chunksize=10**5
prolist=['11','12','13','14','15','21','22','23','31','32','33','34','35','36','37',
          '41','42','43','44','45','46','50','51','52','53','54','61','62','63','64','65']
for data in pd.read_csv(r'E:\data\kf1.csv',names=['name','tp','id','gender',
                                        'birthday','add','mobile','tel','email'],chunksize=chunksize):
    #print(data['id'])
    iddata= data[(data['tp'] == 'ID') & (data['id'].str[:2].isin(prolist))]
    print('----------start-------------')
    #print(iddata)
    id = iddata[['name','id']]
    print(id)
    id.to_csv(r'E:\data\kf_id.txt', sep=' ', mode='a+', encoding='utf-8')
    i += 1
    print(i * chunksize)




