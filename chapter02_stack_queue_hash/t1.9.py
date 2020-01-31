#-*-coding=utf-8-*-
'''
如何从给定的车票中找到旅程。
两个哈希表
'''
def findTrival(tickes):
    Tickes=dict(tickes)
    R_Tickes={Tickes[key]:key for key in Tickes}

    for key in Tickes:
        if key not in R_Tickes:
            begin=key
            break

    print(begin,end='->')
    addr=begin
    while True:
        if addr in Tickes:
            print(Tickes[addr],end='->')
        else:
            break
        addr=Tickes[addr]

if __name__ == '__main__':
    tickes=[('西安','成都'),('北京','上海'),('大连','西安'),('上海','大连')]
    findTrival(tickes)