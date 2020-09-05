

'''
time:月,time:日,loc:小区,loc:超市;5月1号在新龙城或浩客见;月 月 日 日 O 小区 小区 小区 O 超市 超市 O
'''

import sys
test=sys.stdin.readline().strip().split(';')

def entityRecogProcess(text):
    text1=text[0]
    text2=text[1]
    text3=text[2]

    objects=dict()
    objects_set=dict()
    for x in text1.split(','):
        x=x.split(':')
        if x[0] not in objects_set:
            objects_set[x[0]]=set()
        objects_set[x[0]].add(x[1])
        objects[x[1]]=x[0]
    i=0
    text3=text3.split(' ')
    text3=[x for x in text3 if x!=' ']
    result=[]
    while i<len(text3):
        while i<len(text3) and text3[i]=='O':
            i+=1
        if i>=len(text3):
            break
        p=text3[i]
        s=text2[i]
        i=i+1
        while i<len(text3) and text3[i] in objects_set[objects[p]]:
            s+=text2[i]
            i += 1
        result.append('%s:%s' % (objects[p],s))
    return ','.join(result)

print(entityRecogProcess(test))





