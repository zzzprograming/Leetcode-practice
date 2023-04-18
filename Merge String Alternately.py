class Solution(object):
    def mergeAlternately(self, word1, word2):
        i=0 #inital the pointer
        j=0

        result = [] #inital the list for storing resturning pointer values
        while i < len(word1) and j < len(word2): 
            #Use a while loop for pointer to point through all characters in Word1 and Word2
            result.append(word1[i])
            result.append(word2[j])
            #use append to store the pointer value in to our list
            i += 1
            j += 1
            #after each pointing increment to the next character +=1
        result.append(word1[i:])
        result.append(word2[j:])
        #string slice is a way to extract a portion of a string by specifying a range of indices
        #string[start:end:step]
        #In this case we have word1[i:] which means output everything that is after the pointer 

        return "".join(result)

        #use len to count the lengths of the string 
        #learn how to use append function

        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
