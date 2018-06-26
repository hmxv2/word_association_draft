#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import jieba#import bag
import cPickle as pickle
import json
import time
#baidubaike date file
file_path='/home/hmx/baidubaike.json' #get file path
file_handle=open(file_path,'r') #get file handle
'''
a=file_handle.readline()
b=file_handle.readline()
c=json.loads(a)
print a,b,c
print c['para']
'''
#load stopwords list
#stop words
stpwd_handle=open('/home/hmx/Study/Python/SimilarityAndAssociation/stopwords.txt','r')
stpwd_list=list();
for line in open('/home/hmx/Study/Python/SimilarityAndAssociation/stopwords.txt','r'):
    line=stpwd_handle.readline()
    line=line[0:len(line)-1]
    stpwd_list.append(line.encode('utf-8'))
#be a set,faster?
stpwd_list=set(stpwd_list)
print '<' in stpwd_list
print '《' in stpwd_list
print ';' in stpwd_list
print '的' in stpwd_list
print '不' in stpwd_list
print '由' in stpwd_list
stpwd_handle.close()
#cut and save
file_save_handle=open('/home/hmx/Study/Python/SimilarityAndAssociation/data_cut_result.json','a+')
loop_cnt=0
many_lines=[]
#time count
t1=time.time()
#
for line in open(file_path,'r'):
    line=file_handle.readline()
    line=json.loads(line)
    text_data=line['para']#text data
    text_data_seg=jieba.lcut(text_data, cut_all=False) #seg
    text_data_seg_=list()
    for word in text_data_seg:
        if word in stpwd_list:
            continue
        else:
            text_data_seg_.append(word)
    file_save_handle.write(json.dumps(text_data_seg_)+'\n')
    #loop count
    loop_cnt+=1
    if loop_cnt>=5000000:
        break

t2=time.time()
print t2-t1