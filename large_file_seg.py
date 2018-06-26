#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import jieba#import bag
import cPickle as pickle
import json
#
file_path='/home/hmx/baidubaike.json' #get file path
file_handle=open(file_path,'r') #get file handle
'''
a=file_handle.readline()
b=file_handle.readline()
c=json.loads(a)
print a,b
print c['para']
'''
loop_cnt=0
file_number=1
all_lines=[]
for line in open(file_path,'r'):
    line=file_handle.readline()
    line=json.loads(line)
    line_para=line['para']
    all_lines.append(line_para+'\n')
    #
    loop_cnt+=1
    if loop_cnt==1:
        file_save_handle=open('/home/hmx/Study/Python/SimilarityAndAssociation/baidubaike/'+str(file_number)+'.txt','w+')
    if loop_cnt>=5000:
        file_save_handle.writelines(all_lines)
        all_lines=[]
        loop_cnt=0
        file_number+=1
        file_save_handle.close()
        print file_number
    #if file_number>=10:
    #    break
    
#seg

#file_content=file_handle.read() #read file content
#print len(file_content)
#file_content=file_content[1:90000005]#900002,9000005,90000005
#print len(file_content)
#print FileContent #print
#file_content_seg=jieba.lcut(file_content, cut_all=False) #seg
