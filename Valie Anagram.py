class Solution(object):
    def isAnagram(self, s, t):
        #Method 1
        #if sorted(s) == sorted(t): #sorted is a build in function of python
            #return True     
        #return False
         
        #sorted is a build in function of python
        #You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

        #Method 2

        if len(s) != len(t): #first check the length of both words  
            return False
        countS, countT = {}, {} # creating hashmap

        for i in range(len(s)): #loop depends on the length of s because iterat through t depeneds how how many character s have
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

        #countS[s[i]] creating keys for hashmap
        #.get used to return a key value (s[i],0)
        #0 is used as a defult value else a key error will shown 



    








        """
        :type s: str
        :type t: str
        :rtype: bool
        """
