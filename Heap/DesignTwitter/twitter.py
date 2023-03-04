from collections import defaultdict
from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.user_dict = defaultdict(list) # userID: [followeeIDs]
        self.tweets = [] # priority queue, Tweet() object
        self.priority_num = 0 # will decrement by 1 each time a new tweet coming in, so newest tweet stays on top of the heap (min heap)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.priority_num -= 1
        heapq.heappush(self.tweets, [self.priority_num, userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        checked = []

        while self.tweets and len(res) < 10:
            priority, tweeterID, tweetID = heapq.heappop(self.tweets)
            if tweeterID==userId or tweeterID in self.user_dict[userId]:
                res.append(tweetID)
            checked.append([priority, tweeterID, tweetID])

        for tweet in checked:
            heapq.heappush(self.tweets, tweet)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # if self.user_dict.get(followeeId) is None:
        #     self.user_dict[followeeId] = []
        self.user_dict[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_dict[followerId]:
            self.user_dict[followerId].remove(followeeId)