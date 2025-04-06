class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Get the length of the input list
        n = len(nums)

        # In case k is greater than n, use modulus to get the effective number of rotations
        k = k % n

        # Create a new list to hold the rotated version of nums
        rotated = [0] * n

        # Place each element at its new position in the rotated list
        for i in range(n):
            # Calculate the new index using (i + k) % n and place nums[i] there
            rotated[(i + k) % n] = nums[i]

        # Copy the rotated list back into the original list
        for i in range(n):
            nums[i] = rotated[i]
