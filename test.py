#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import jieba#import bag
import cPickle as pickle
import json
#
f=open('a.json','w+')
d1=['a','b']#{'a':1,'b':2}
d2=['c','d']#{'c':3,'d':4}
d1=json.dumps(d1)
d2=json.dumps(d2)
f.write(d1+'\n')
f.write(d2+'\n')
f.close()

#read
f=open('a.json','r')
for line in open('a.json','r'):
    line=f.readline()
    tmp=json.loads(line)
    print tmp
f.close()
'''
输出结果如下，说明readline读到的换行符并不影响loads的转换效果
{u'a': 1, u'b': 2}
{u'c': 3, u'd': 4}
'''