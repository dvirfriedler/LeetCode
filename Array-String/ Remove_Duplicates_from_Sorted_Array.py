from typing import List

'''
Link:  https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[p] = nums[i]
                p +=1
        return p
                


         
         

 
            


        
        







        
        



     

        




    

       

    


            

            
            


       
            
          
            
        

           
                







        
        
        
        

        
        
        
        
        






