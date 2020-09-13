'''
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack=[]
        self._minStack=[]
        self._size=0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._stack.append(x)
        if self._size==0 or self._minStack[-1]>x:
            self._minStack.append(x)
        else:
            self._minStack.append(self._minStack[-1])
        self._size+=1



    def pop(self):
        """
        :rtype: None
        """
        if self._size>0:
            self._stack.pop()
            self._minStack.pop()
            self._size-=1


    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self._minStack[-1]


if __name__ == '__main__':
    s=MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())
    s.pop()
    print(s.top())
    print(s.getMin())
