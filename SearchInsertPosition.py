
'''
link - https://leetcode.com/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-interview-150

Problem: 
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Sultion:

Approach:  Binary Search


'''

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Edge cases
        if nums[-1] < target:
            return len(nums)
        
        elif nums[0] >= target:
            return 0
        

        start,end = 0, len(nums) - 1

        while(start < end):
            idx = start + (end - start) // 2

            current = nums[idx]

            if current  == target:
                return idx

            elif current < target:
                start = idx + 1

            else: #current > target
                end = idx - 1

        if nums[end] < target:
            return end + 1
        else:
            return end
        
        
def Test(nums: List[int], target: int, expected: int) -> None:
    s = Solution()
    ans = s.searchInsert(nums, target)
    
    if ans == expected:
        print('Test Passed')
        
    else:
        print('Test Failed')
        print(f'Expected: {expected}, Got: {ans}')
       
# Test
Test([1,3,5,6], 5, 2) 
Test([1,3,5,6], 2, 1)
Test([1,3,5,6], 7, 4)
Test([1,3,5,6], 0, 0)
Test([1,3], 2, 1)
Test([1,2,4,6,7], 3, 2)
        


        






    
    


