from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_counts = Counter(nums) #establish a counter
        elem_dict = dict(element_counts) #check dictionary
        for k,v in elem_dict.items(): #for loop
            if v >len(nums)/2: # check the condition again, why v ask urself, v tells us how many times it appears? 
                return k
        