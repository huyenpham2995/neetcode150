### Question
[Link to question.](https://leetcode.com/problems/koko-eating-bananas/)

### Thoughts
- Input and output:
    - Input: list of heights of each retangle.
    - Output: the area of the largest rectangle that can be created.
- If the piles of bananas is equal to the time constraint, then the result is the maximum bananas in the piles, since you have to finish all bananas of 1 pile in an hour.
- The trick comes when Koko can finish earlier than that, she can eat less. And the number of bananas she eat each hour does not have to be one of the number of bananas in the piles. So instead of doing binary search with the number in the piles, we do binary search of the number from 1 up to k.
    - I got trapped in thinking the range should be the min # of bananas in the pile and max # of bananas in the pile, but it's actually starting from 1. Why? For example: [500], h=499. the min # in the pile is 500, and she can finish eating in 1 hour. But actually she can just eat 2 bananas per hour and still make it until the guard comes back, and 2 is not the min the pile.
- Process of finding that number:
    - Let the min banana = 1 and max banana = max # of banana in the pile (koko shouldn't eat more than the maximum number)
    - Get the middle point of that and go through the piles, calculate how many hours she needs to finish each pile. Sum that number up and compare it to the time constrain.
    - Adjust the left side or right side of the boundary based on the number.
    - Another tricky part: when the time added up to h, we can actually still decrease the # of bananas Koko eat and the time will still stay the same. So instead of returning when we find the # of bananas that Koko eat that added up to h, we have to scan until we exhaust every numbers, which is when left boundary > right boundary.

### BigO
- binary search from 1 to max(piles) = k takes O(logk).
- Each time we get a speed, we go through the piles to calculate the time => O(nlogk).