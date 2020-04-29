'''
#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
题目描述：
求a+b的和
输入描述：
多组输入，每一行有两个数A，B。
输出描述：
每一行输出一个结果。

import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))

题目描述：
给出n阶方阵里所有数，求方阵里所有数的和。
输入描述：
输入有多个测试用例，每个测试用例第一行为一个整数n(n<1000),表示方阵的阶数为n,接下来是n行数字，每行n个数字用空格隔开
输出描述：
给出一个整数，表示结果。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)
'''


