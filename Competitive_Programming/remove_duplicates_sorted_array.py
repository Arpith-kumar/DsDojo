# Remove Duplicates from Sorted Array


# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        temp = 1
        for a, b in zip(nums, nums[1:]):
            if a != b:
                nums[temp] = b
                temp += 1
        return temp
