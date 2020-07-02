'''
实现一个拥有如下方法的线程安全有限阻塞队列：

BoundedBlockingQueue(int capacity) 构造方法初始化队列，其中capacity代表队列长度上限。
void enqueue(int element) 在队首增加一个element. 如果队列满，调用线程被阻塞直到队列非满。
int dequeue() 返回队尾元素并从队列中将其删除. 如果队列为空，调用线程被阻塞直到队列非空。
int size() 返回当前队列元素个数。
你的实现将会被多线程同时访问进行测试。每一个线程要么是一个只调用enqueue方法的生产者线程，
要么是一个只调用dequeue方法的消费者线程。size方法将会在每一个测试用例之后进行调用。

请不要使用内置的有限阻塞队列实现，否则面试将不会通过。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-bounded-blocking-queue
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from threading import Semaphore
from collections import deque
class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.data=deque()
        self.mutex=Semaphore(1) # 互斥访问
        self.full=Semaphore(0)  # 同步
        self.empty=Semaphore(capacity) # 同步

    def isEmpty(self):
        return len(self.data)==0

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        self.empty.release()
        self.mutex.acquire()
        self.data.append(element)
        self.mutex.release()
        self.full.release()

    def dequeue(self):
        """
        :rtype: int
        """
        self.full.acquire()
        self.mutex.acquire()
        val=self.data.popleft()
        self.mutex.release()
        self.empty.acquire()
        return val

    def size(self):
        """
        :rtype: int
        """
        return len(self.data)
