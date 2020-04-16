'''
插入排序
'''

def insert_sort(X):
    result=[X[0]]
    for x in X[1:]:
        i=0
        while i<len(result):
            if result[i]>x:
                break
            i+=1
        result.insert(i,x)
    return result

if __name__ == '__main__':
    import random

    X = [random.randint(10, 30) for _ in range(40)]
    print(X)
    print(insert_sort(X))
