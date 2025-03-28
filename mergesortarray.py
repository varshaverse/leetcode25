class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Merge nums2 into nums1
        for i in range(n):
            nums1[m + i] = nums2[i]
        
        # Sort the merged nums1 array
        nums1.sort()
        
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

# Get input from the user
# Input for nums1, nums2, m, n
nums1 = list(map(int, input("Enter the elements of nums1 (including space for extra zeros): ").split()))
m = int(input("Enter the number of valid elements in nums1 (m): "))
nums2 = list(map(int, input("Enter the elements of nums2: ").split()))
n = len(nums2)  # n is the length of nums2

# Create an instance of the Solution class
solution = Solution()

# Call the merge method
solution.merge(nums1, m, nums2, n)

# Print the result after merging and sorting
print("Merged and sorted nums1:", nums1)
