'''
Tuple with Same Product
Given an array nums of distinct positive integers,
 return the number of tuples (a, b, c, d) such that 
 a * b = c * d where a, b, c, and d are elements of
 nums, and a != b != c != d.
Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.

'''

#todo, debug and try aproches withot defaultdict
from collections import defaultdict

def tupleSameProduct(self, nums: list[int]) -> int:
    cnt = defaultdict(int)
    for i in range(1, len(nums)):
        for j in range(i):
            x = nums[i] * nums[j]
            cnt[x] += 1
    return sum(v * (v - 1) // 2 for v in cnt.values()) << 3