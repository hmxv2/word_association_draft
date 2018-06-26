#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import jieba#import bag
import cPickle as pickle
import json
import time
#baidubaike date file
file_handle=open('/home/hmx/Study/Python/SimilarityAndAssociation/backups/data_cut_result.json(500w)','r') #get file handle

assciation_window=5
dict_of_assciation_word={}
dict_of_every_word={}
loop_control=0
#time count
#starting timestamp
t1=time.time()
for text_data in open('/home/hmx/Study/Python/SimilarityAndAssociation/backups/data_cut_result.json(500w)','r'):
    text_data = file_handle.readline()
    text_data=json.loads(text_data)#now text_data is list
    #print u" ".join(text_data)
    words_num=len(text_data)
    word_idx=0
    while word_idx<words_num:
        #print word_idx
        word_target=text_data[word_idx]
        if word_target not in dict_of_assciation_word:
            dict_of_assciation_word[word_target]={}
        
        if word_target not in dict_of_every_word:
            dict_of_every_word[word_target]=1
        else:
            dict_of_every_word[word_target]+=1
            '''
        if word_idx-assciation_window>=0:
            loop_cnt=1
            while loop_cnt<=assciation_window:
                if text_data[word_idx-loop_cnt] in dict_of_assciation_word[word_target]:
                    dict_of_assciation_word[word_target][text_data[word_idx-loop_cnt]]+=1
                else:
                    dict_of_assciation_word[word_target][text_data[word_idx-loop_cnt]]=1
                loop_cnt+=1
        if word_idx+assciation_window<words_num:
            loop_cnt=1
            while loop_cnt<=assciation_window:
                if text_data[word_idx+loop_cnt] in dict_of_assciation_word[word_target]:
                    dict_of_assciation_word[word_target][text_data[word_idx+loop_cnt]]+=1
                else:
                    dict_of_assciation_word[word_target][text_data[word_idx+loop_cnt]]=1
                loop_cnt+=1
    '''
        word_idx=word_idx+1
       
    loop_control+=1
    if loop_control>=4000002:
        break
#ending timestamp
t2=time.time()
#
#for word in dict_of_every_word:
#    print word,dict_of_every_word[word]
print '的' in dict_of_every_word
print '《' in dict_of_every_word
#print running time
print 'running time:%f'%(t2-t1)
file_handle.close()

#
t1=time.time()
#save as file
f_save_path='/home/hmx/Study/Python/SimilarityAndAssociation/tmp/'
f1=open(f_save_path+'dict_of_every_word.txt','w+')
#f2=open(f_save_path+'dict_of_association_word.txt','w+')
f1.write(json.dumps(dict_of_every_word))
#f2.write(json.dumps(dict_of_assciation_word))
f1.close()
#f2.close()
t2=time.time()
print 'file saving time:%f'%(t2-t1)
