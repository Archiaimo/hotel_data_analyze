import jieba
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import numpy as np
from PIL import Image

textfile=open(r'E:\data\firstname.txt','r',encoding='gbk',errors='ignore')#加载文本
wordslist =textfile.readlines()
wordstr=str(wordslist).replace('\\t','')
#print(wordstr)

wordlist =jieba.cut(wordstr,cut_all=True)#切割
space_list=" ".join(wordlist)#链接词语
#print(space_list)

background =np.array(Image.open(r'E:\images\color.png'))#背景图片
mywordcloud =WordCloud(width=1000,height=1000,
                       background_color='white', #背景颜色
                       mask=background, #从背景图中提取颜色
                       max_words=100, #最大词语数量
                       stopwords=STOPWORDS,#停止的默认词语
                       font_path='simsun.ttc',#字体
                       max_font_size=200,#最大字体尺寸
                       random_state=30,#随机角度
                       scale=2).generate(space_list)#生成词云
image_color=ImageColorGenerator(background)#从背景图片中提取颜色
plt.imshow(mywordcloud)#显示词云
plt.axis('off')#关闭保存
plt.show()#



