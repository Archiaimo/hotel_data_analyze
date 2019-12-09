import pandas_profiling
import pandas as pd

chunksize = 10**5

for data in pd.read_csv(r'E:\data\kf1.csv',chunksize=chunksize):

    profile=data.profile_report()
profile.to_file(output_file='kf_report.html')
