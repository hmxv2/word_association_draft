#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import jieba#import bag
import pickle
#
file_path='/home/hmx/baidubaike_1w.json' #get file path
file_handle=open(file_path,'r') #get file handle


file_content=file_handle.read() #read file content
print len(file_content)
#file_content=file_content[1:90000005]#900002,9000005,90000005
print len(file_content)
#print FileContent #print
file_content_seg=jieba.lcut(file_content, cut_all=False) #seg


#stop words
stpwd_handle=open('/home/hmx/Study/Python/SimilarityAndAssociation/stopwords.txt','r')
stpwd_list=list();
for line in open('/home/hmx/Study/Python/SimilarityAndAssociation/stopwords.txt','r'):
    line=stpwd_handle.readline()
    stpwd_list.append(line.encode('utf-8'))
#print
#stpwd_list=set(stpwd_list)
print ("“"+"\n") in stpwd_list
print ("-"+"\n") in stpwd_list
print ("与"+"\n") in stpwd_list

#remove the stopwords
file_content_seg_tmp=list()
for word in file_content_seg:
    if (word+'\n') in stpwd_list:
        continue
    else:
        file_content_seg_tmp.append(word)
file_content_seg=file_content_seg_tmp

#
#print u" ".join(file_content_seg) #print
file_save_handle=open('FileContentAfterCut.txt', 'w+')
print 'file saving...'
print >>file_save_handle,u" ".join(file_content_seg) #write
print 'file saved!'
#close files
file_save_handle.close()
file_handle.close() #close file
stpwd_handle.close()
#
print "number of words:%d" %len(file_content_seg)

'''
#save variables
print 'saving variables...'
pickle.dump(file_content_seg,open('file_content_seg.txt','wb'))
print 'variables saved!'
'''

#mutual information
words_num=len(file_content_seg)
word_idx=0
assciation_window=5
dict_of_assciation_word={}
dict_of_every_word={}
while word_idx<words_num:
    #print word_idx
    word_tag=file_content_seg[word_idx]
    if word_tag not in dict_of_assciation_word:
        dict_of_assciation_word[word_tag]={}
        
    if word_tag not in dict_of_every_word:
        dict_of_every_word[word_tag]=1
    else:
        dict_of_every_word[word_tag]+=1
    if word_idx-assciation_window>=0:
        loop_cnt=1
        while loop_cnt<=assciation_window:
            if file_content_seg[word_idx-loop_cnt] in dict_of_assciation_word[word_tag]:
                dict_of_assciation_word[word_tag][file_content_seg[word_idx-loop_cnt]]+=1
            else:
                dict_of_assciation_word[word_tag][file_content_seg[word_idx-loop_cnt]]=1
            loop_cnt+=1
    if word_idx+assciation_window<words_num:
        loop_cnt=1
        while loop_cnt<=assciation_window:
            if file_content_seg[word_idx+loop_cnt] in dict_of_assciation_word[word_tag]:
                dict_of_assciation_word[word_tag][file_content_seg[word_idx+loop_cnt]]+=1
            else:
                dict_of_assciation_word[word_tag][file_content_seg[word_idx+loop_cnt]]=1
            loop_cnt+=1
    
    word_idx=word_idx+1
    
print 'dict_of_assciation_word:%d' %len(dict_of_assciation_word)
print 'dict_of_every_word:%d' %len(dict_of_every_word)
#
word_ass_num=0.0
word_x=' '
word_ass=' '
mutual_times_threshold=10
mutual_info_threshold=64
result={}
for word in dict_of_assciation_word:
    for word_ in dict_of_assciation_word[word]:
        if dict_of_assciation_word[word][word_]<mutual_times_threshold:
            continue
        tmp=dict_of_assciation_word[word][word_]*1.0/dict_of_every_word[word]/dict_of_every_word[word_]*words_num
        if tmp>mutual_info_threshold:
            if word in result:
                result[word][word_]=tmp
            else:
                result[word]={}
                result[word][word_]=tmp
            '''
            word_ass=word_
            word_ass_num=tmp
            word_x=word
            print dict_of_assciation_word[word][word_],dict_of_every_word[word],dict_of_every_word[word_]
        
print word_x,word_ass,word_ass_num
print dict_of_assciation_word[word_x][word_ass],dict_of_every_word[word_x],dict_of_every_word[word_ass]
    '''
file_save_handle=open('result.txt','w+')
print 'file saving...'
for word_x in result:
    for word_ass in result[word_x]:
        #print word_x,word_ass,result[word_x][word_ass]
        print >>file_save_handle,word_x,word_ass,result[word_x][word_ass]
print 'file saved!'
file_save_handle.close()    
'''
file_content=file_handle.read() #read file content
file_content=file_content[1:9002]
for line in file_content_line.readline():
    line_seg=jieba.cut(line, cut_all=False) #seg
    file_save_handle.write(u' ',join(line_seg));
'''





