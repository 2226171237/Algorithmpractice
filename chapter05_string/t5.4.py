'''
判断两个字符串是否为换位字符串
'''
# 方法1:hash_dict
def compare(s1,s2):
    hash_d=dict()
    for s in s1:
        if s in hash_d:
            hash_d[s]+=1
        else:
            hash_d[s]=1
    for s in s2:
        if s in hash_d:
            hash_d[s]-=1
        else:
            hash_d[s]=1
    for s in hash_d:
        if hash_d[s]>0:
            return False
    return True

if __name__ == '__main__':
    s1='aacbc'
    s2='abcac'
    print(compare(s1,s2))