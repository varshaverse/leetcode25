class Solution(object):
    def removeElement(self, nums, value):
        c = 0  # Pointer tracks the elements

        for i in range(len(nums)):
            if nums[i] != value:
                nums[c] = nums[i]
                c += 1  # Increment only when an element is kept

        return c

# Input handling
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    value = int(input("Enter the value to remove: "))

    sol = Solution()
    new_length = sol.removeElement(nums, value)

    print(f"New array length: {new_length}")
    print(f"Modified array: {nums[:new_length]}")




#class Solution(object):
    #def removeElement(self, nums, value):
        #c = 0 #pointer tracks the elements

        #for i in range(len(nums)):
            #if nums[i] != value:
                #nums[c] = nums[i]
            #c += 1
        #return c

        

