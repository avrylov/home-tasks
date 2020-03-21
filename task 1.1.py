import re
import numpy as np
file_obj = open('C:\Users\user\Desktop\sentences.txt')
data_list = file_obj.readlines()
m=[]
for line in data_list:
    line.strip().lower()
    mylist=filter(None, re.split('[^a-z]', line.strip().lower()))
    m.append(mylist)

i=[]
for element in m:
    for word in element:
        i.append(word)#все слова в один список

word = list(set(i))
d=dict((word, index) for index, word in enumerate(word))#словарь уникальных слов

h=[]
for element in m:
    luch=np.zeros(len(d))
    for word in element:
        luch[d[word]]=1
    h.append(luch)
h1=np.array(h)

from scipy.spatial import distance
m1=[]
v1=h1[0:1]
for v in h1:
    cos=distance.cosine(v1,v)
    m1.append(cos)
for cos1 in list(enumerate(m1)):
    print cos1