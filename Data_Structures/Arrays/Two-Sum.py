



def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = []

    for r, i in enumerate(nums):
        for c, j in enumerate(nums):
            if i+j == target and r != c:
                result.append(r)
                result.append(c)
                return result


print(twoSum([3, 2, 4], 6))

#enumetate gives index and item
