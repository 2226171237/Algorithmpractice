'''
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
调用 min、push 及 pop 的时间复杂度都是 O(1)。
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data=[]
        self.minStack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if len(self.minStack)==0:
            self.minStack.append(x)
        else:
            x=min(self.minStack[-1],x)
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.minStack.pop()
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.minStack[-1]