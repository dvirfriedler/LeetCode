from typing import List

'''
Link:  https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                count +=1
                nums[pointer] = nums[i]
                pointer +=1
        return count 
            


        
        







        
        



     

        




    

       

    


            

            
            


       
            
          
            
        

           
                







        
        
        
        

        
        
        
        
        






