from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: If the array is empty, return 0
        if not nums:
            return 0
        
        # unique_index tracks the position of unique elements, scanner scans the array
        unique_index, scanner = 0, 1
        
        # Iterate through the list using the scanner pointer
        while scanner < len(nums):  # Changed 'scanner in range(len(nums))' to 'scanner < len(nums)'
            # If duplicate element is found, move the scanner pointer forward
            if nums[unique_index] == nums[scanner]:
                scanner += 1
            else:
                # If a new unique element is found, move it next to the last unique element
                unique_index += 1  # Move unique_index first to avoid overwriting itself
                nums[unique_index] = nums[scanner]
                scanner += 1

        # The length of the modified array with unique elements is unique_index + 1
        return unique_index + 1

