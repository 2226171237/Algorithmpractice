

# 从一个链表中均匀抽样一个样本

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head=head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res=self.head
        i=0
        node=self.head
        while node:
            if random.randint(0,i)==0:
                res=node
            node=node.next
            i+=1
        return res.val


# 给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。
# 注意：
# 数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。
class Solution2(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums

    def pick(self, k):
        """
        :type k: int
        :rtype: int
        """
        res=[i for i in range(k)]
        for i in range(k,len(self.nums)):
            rand_i=random.randint(0,i)
            if rand_i<k:
                res[rand_i]=i
        return res

s=Solution2([1,2,3,4,5,6,7,8,9,10])
print(s.pick(6))

# 数据打撒
def shuffle(nums):
    for i in range(len(nums)-1):
        j=random.randint(i,len(nums)-1)
        nums[i],nums[j]=nums[j],nums[i]

nums=[1,2,3,4,5,6,7,8,9]
shuffle(nums)
print(nums)

