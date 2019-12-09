import pandas as pd

i=0
chunksize=10**6
mobileList = ['130', '131', '132', '145', '155', '156', '166', '171', '175', '176', '185', '186', '134', '135',
                 '136', '137', '138', '139', '147', '150', '151', '152', '157', '158', '159', '172', '178', '182',
                 '183', '184', '187', '188', '198', '133', '149', '153', '173', '177', '180', '189', '181', '191',
                 '199']
for data in pd.read_csv(r'E:\data\kf1.csv',names=['name','tp','id','gender',
                                        'birthday','add','mobile','tel','email'],chunksize=chunksize):
    mobiledata = data
    mobiledata['mobile']=mobiledata['mobile'].astype(str)
    mobiledata=mobiledata[mobiledata['mobile'].astype(str).str[:3].isin(mobileList)]
    print('------------')
    mobile=mobiledata[['name','mobile']]
    mobile.to_csv(r'E:\data\kf_mobile.txt', sep=' ', mode='a+', encoding='utf-8')
    i += 1
    print(i*chunksize)
