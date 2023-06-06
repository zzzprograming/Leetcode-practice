class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set() #creating a set to store 

        for n in nums: #for loop to run through all the numbers in the set
            if n in hashset: #if the number exist in the set then true 
                return True 
            hashset.add(n) #if not then add and return false 
        return False

        #this questions use hashset
        #To check if the number already exist in the hashset
        #if they exist then return true if not add the number to the set
        #This way it save time and space
        #Time: O(n)
        #Space: O(n)
        
