from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_counts = Counter(nums)
        elem_dict = dict(element_counts)
        for k,v in elem_dict.items():
            if v>len(nums)/2:
                return k
        