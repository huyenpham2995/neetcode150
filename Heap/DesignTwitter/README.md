### Question
- [Link to question.](https://leetcode.com/problems/design-twitter/description/)

### Thoughts
- What we need:
    - Something to keep track of a user and all the people that they followed. Preferably a dictionary with key as followerID, value as the list of followeeIDs.
    - A structure to keep all the tweets. Since we need to retrieve the most recent posted tweets, we can create a heap with priority number attached to each tweets. Each component of tweet have the following:
        - TweetId
        - UserId (the Id of the user who posted that tweet)
        - priority number: this will be kept track by the class. Each time a new tweet comes in, it will be assign a number that is smaller than the number of the tweet that was posted right before it. So when we build a min heap, that tweet will be above the previous tweet.
    - Post tweet:
        - When a new tweet come in, calculat its priority number.
        - Then push [priority number, userId, tweetId] to the heap.
    - Follow:
        - Append the followeeId to dict[followerId].
    - Unfollow:
        - Check to see if the user have followed that Id before (we can only unfollow when we follow someone before). If yes, pop the followeeId out of the list dict[followerId].
    - Get New Feeds:
        - This is the trickiest since we need to obtain the latest 10 tweets, and these tweets need to be from the user themselve or someone they are following.
        - Corner case: there's not enough 10 tweets from those people => take all the tweets that you can, i.e if the heap is empty stop the operation.
        - So when the heap is not empty and we still don't have enough 10 tweets:
            - pop the tweet from the min heap. The top of the heap indicate the latest tweet (based on the priority number)
            - See if the userId (i.e the one who posted that tweet) matches the userId of the one that request to get news feed, or in the list of all the people that they follow. If yes, add that tweetId to the result.
            - Add the tweet to a list so later we can add them back to the heap.
        - After we have all the tweets we need, get the list that we just popped and add it back to the heap for future operation.
        - Return the result list.

### BigO
- Post tweet takes O(LogN), with N being the number of tweets, since we need to reheap up/down.
- Follow takes O(1) time (find the user in the dictionary take 1 action, add the followee to the list take 1 action).
- Unfollow takes O(1) time (find the user in the dictionary take 1 action, remove the followee if they are in the list take 1 action)
- get new feeds takes at most N times to pop out the tweets, then at most NlogN time to add them back to the heap.