'''
假设有这么一个类：
class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // 构造函数
  public void zero(printNumber) { ... }  // 仅打印出 0
  public void even(printNumber) { ... }  // 仅打印出 偶数
  public void odd(printNumber) { ... }   // 仅打印出 奇数
}
相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程：

线程 A 将调用 zero()，它只输出 0 。
线程 B 将调用 even()，它只输出偶数。
线程 C 将调用 odd()，它只输出奇数。
每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为 2n。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/print-zero-even-odd
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import threading
from threading import Semaphore
class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n+1
        self.Zero=Semaphore(1)
        self.Even=Semaphore(0)
        self.Odd=Semaphore(0)
    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n):
            self.Zero.acquire()
            printNumber(0)
            if i%2==0:
                self.Even.release()
            else:
                self.Odd.release()  # V

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n):
            if i%2==0:
                self.Even.acquire()
                printNumber(i)
                self.Zero.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n):
            if i%2!=0:
                self.Odd.acquire()  # P
                printNumber(i)
                self.Zero.release()

def printf(x):
    print(x,end='')

s=ZeroEvenOdd(20)
t1=threading.Thread(target=s.zero,args=(printf,))
t2=threading.Thread(target=s.even,args=(printf,))
t3=threading.Thread(target=s.odd,args=(printf,))

t1.start()
t2.start()
t3.start()
