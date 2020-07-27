
import heapq

class User:
    def __init__(self,id):
        self.id=id
        self.follows=set()
        self.tweet_head=None
        self.follows.add(self.id) # 关注自己

    def follow(self,userId):
        self.follows.add(userId)

    def unfollow(self,userId):
        if userId!=self.id:
            self.follows.remove(userId)

    def post(self,tweetId,time):
        node=Tweet(tweetId,time)
        node.next=self.tweet_head
        self.tweet_head=node

class Tweet:
    def __init__(self,id,time):
        self.id=id
        self.time=time
        self.next=None
    def __lt__(self, other):
        return self.time>other.time
    def __gt__(self, other):
        return self.time<other.time

class Twitter:
    timestamp=0
    def __init__(self):
        self.usermap=dict() # user_i->user

    def postTweet(self,userId,tweetId):
        if userId not in self.usermap:
            user=User(userId)
            self.usermap[userId]=user
        user=self.usermap.get(userId)
        Twitter.timestamp+=1
        user.post(tweetId,Twitter.timestamp)

    def getNewsFeed(self,userId):
        res=[]
        heap=[]
        if userId not in self.usermap:
            return res
        users=self.usermap[userId].follows
        for user in users:
            tweet=self.usermap[user].tweet_head
            if tweet:
                heapq.heappush(heap,tweet)
        while len(heap):
            if len(res)==10:
                break
            t=heapq.heappop(heap)
            res.append(t.id)
            if t.next:
                heapq.heappush(heap,t.next)
        return res

    def follow(self,follwerId,followeedId):
        if followeedId not in self.usermap:
            user=User(follwerId)
            self.usermap[follwerId]=user
        if followeedId not in self.usermap:
            user=User(followeedId)
            self.usermap[followeedId]=user
        self.usermap[follwerId].follow(followeedId)

    def unfollow(self,follwerId,followeedId):
        if follwerId in self.usermap:
            self.usermap[follwerId].unfollow(followeedId)


if __name__ == '__main__':
    twitter=Twitter()
    twitter.postTweet(1,1)
    twitter.postTweet(2,2)
    twitter.follow(1,2)
    twitter.postTweet(3,4)
    twitter.postTweet(3,2)
    print(twitter.getNewsFeed(1))