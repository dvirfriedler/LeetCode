
'''
link - https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150

Problem: 
You are given an m x n integer matrix matrix with the following two properties:

*   Each row is sorted in non-decreasing order.
*   The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Sultion:

Approach:  Binary Search on the  min and max values of the rows and then inside the row 
'''

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def find_row(matrix: List[List[int]], target: int):
            r_start, r_end = 0, len(matrix) - 1
            
            while (r_start < r_end):
                r_current = r_start + (r_end - r_start) // 2
                
                if matrix[r_current][0] <= target <= matrix[r_current] [-1]:
                    return r_current

                elif target < matrix[r_current][0]: # target < min value of this row
                    r_end = r_current - 1

                else: # target >  matrix[r_current][-1] (target > max value of this row)
                    r_start = r_current + 1
                    
            if matrix[r_start][0] <= target <= matrix[r_start][-1]:
                return r_start

            return -1


        # target < minimum or target > maximum
        if target < matrix[0][0] or target > matrix[-1][-1]: 
            return False

        row_index = find_row(matrix,target)

        if row_index == -1: return False

        start, end  = 0, len(matrix[0]) -1

        while (start < end):
            idx = start + (end -start)//2
            current = matrix[row_index][idx]
            if target == current:
                return True

            elif target > current:
                start = idx + 1
            
            else: # target < current
                end = idx - 1

        return matrix[row_index][end] == target
       
        
def Test(matrix: List[List[int]], target: int, expected: bool) -> None:
    s = Solution()
    ans = s.searchMatrix(matrix, target)
    
    if ans == expected:
        print('Test Passed')
        
    else:
        print('Test Failed')
        print(f'Expected: {expected}, Got: {ans}') 
       
# Test
Test([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True)
Test([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False)
Test([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60, True)
Test([[1]], 1, True)


        






    
    


