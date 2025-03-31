from typing import List

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize two pointers: slow tracks the position of unique elements, fast scans the array
        slow, fast = 0, 1
        
        # Iterate through the list using the fast pointer
        while fast in range(len(nums)):
            # If duplicate element is found, move the fast pointer forward
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                # If a new unique element is found, move it next to the last unique element
                nums[slow + 1] = nums[fast]
                fast += 1
                slow += 1

        # The length of the modified array with unique elements is slow + 1
        return slow + 1
