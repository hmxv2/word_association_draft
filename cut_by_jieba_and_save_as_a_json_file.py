#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import jieba#import bag
import cPickle as pickle
import json
import time
#
file_save_path='/home/hmx/Study/Python/SimilarityAndAssociation/cut_by_jieba.json'
file_save_handle=open(file_save_path,'a+')
#
file_path='/home/hmx/Study/Python/SimilarityAndAssociation/baidubaike/' #get file path
#load stopwords list
#stop words
stpwd_handle=open('/home/hmx/Study/Python/SimilarityAndAssociation/stopwords.txt','r')
stpwd_list=list();
for line in open('/home/hmx/Study/Python/SimilarityAndAssociation/stopwords.txt','r'):
    line=stpwd_handle.readline()
    #line=line[0:len(line)-1]
    stpwd_list.append(line.encode('utf-8'))

print '<\n' in stpwd_list
print '《\n' in stpwd_list
print ';\n' in stpwd_list
stpwd_handle.close()
#for w in stpwd_list:
#    print w
t1=time.time()
total_number_of_files=40
for file_number in [x+1 for x in range(total_number_of_files)]:
    file_handle=open(file_path+str(file_number)+'.txt','r')
    file_content=""
    for line in open(file_path+str(file_number)+'.txt','r'):
        line=file_handle.readline()
        file_content=file_content+line
    file_content_seg=jieba.lcut(file_content, cut_all=False) #seg
    file_content_seg_tmp=list()
    idx=0
    for word in file_content_seg:
        if (word+'\n') in stpwd_list:
            continue
        else:
            file_content_seg_tmp.append(word)
        '''
        if (word) in stpwd_list:# a stopword, remove it
            file_content_seg.pop(idx)
        idx+=1
        '''
    #
    #print u" ".join(file_content_seg_tmp)
    file_save_handle.write(json.dumps(file_content_seg_tmp)+'\n')

file_save_handle.close()

t2=time.time()
print t2-t1