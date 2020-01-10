import codecs    #转码
import os
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#from wordcloud import WordCloud
import matplotlib.pyplot as plt
from jieba import analyse

#os.chdir('E:\\')  #更改当前工作目录
#读取停用词
stopwords = codecs.open('./stopwords.txt','r').read()
#读取小说内容
text = codecs.open('./monogatari.txt','r').read()

#对文本进行清理 停用词等
def process_words(text,stopwords):
    mywordlist = []
    #整理数据
    seg_list = jieba.cut(text,cut_all = False)#进行分词 默认精确分词
    liststr = '/ '.join(seg_list)  #把分词的结果放到同一个变量
    #print(liststr)
    for myword in liststr.split('/'):
        if not (myword.strip() in stopwords) and len(myword.strip())>1:
            mywordlist.append(myword)
    return (''.join(mywordlist))
final_words = process_words(text,stopwords)  #生成解析结果

#绘制词云
wid=14000
hei=int(wid/1.777777777777777)-500
col='black'
wordcloud = WordCloud(font_path = './iekie_baijiaheiiti.ttf'#中文字体路径,
                    ,background_color = col#背景颜色
                     ,max_words=5000
                     ,width = wid
                     ,height = hei
                     #,mask = back_coloring  #词云的形状
                     ,margin = 2).generate(final_words)

plt.figure(figsize = (12,12))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file("./wordcloud_"+col+".jpg")