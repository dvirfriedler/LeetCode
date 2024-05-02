from typing import List

'''
Link:  https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0: return nums1

        m = m - 1
        n = n - 1
        j = len(nums1) - 1
    
        while j > -1:
            if m == -1:
                while n > -1:
                    nums1[j] = nums2[n]
                    n-=1
                    j-=1
            if nums1[m] > nums2[n] or n == -1:
                nums1[j] = nums1[m]
                m -=1
            else:
                nums1[j] = nums2[n]
                n -=1
            j-=1
            


        
        







        
        



     

        




    

       

    


            

            
            


       
            
          
            
        

           
                







        
        
        
        

        
        
        
        
        






