#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import jieba#import bag
import cPickle as pickle
import json
import time

file_path='/home/hmx/Study/Python/SimilarityAndAssociation/cut_by_jieba.json'
file_handle=open(file_path,'r')
words_list=[]
t=0
t1=time.time()
for line in open(file_path,'r'):
    line=file_handle.readline()
    line=json.loads(line[:-1])
    #print u" ".join(line)
    #words_list.append(line)
    t+=1
print t

t2=time.time()
print t2-t1
#print u" ".join(words_list)

file_handle.close()
'''
hd=open('a.txt','w+')
hd.writelines(['a'])
hd.close()
hd=open('a.txt','r')
re=hd.readline()
print re
'''

