import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.sans-serif']=['SimHei']

proallseries.index=pronamelist

proallseries=proallseries.sort_values(ascending=False)

fig=proallseries.plot(kind='bar')