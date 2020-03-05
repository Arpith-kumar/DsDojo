'''
algorithm : floyd's tortoise and hare
finding the duplicate number in an array of size n+1 given n integers from 1 to n
time complexity O(nlog(n))
space complexity O(1)
'''
def findDuplicates(nums):
    torties=nums[0] #initilize tortoies to the first item in the list
    hare=nums[0]    #same for hare
    while True: 
        torties = nums[torties] #make tortoies travel 
        hare = nums[nums[hare]] #make hare travel twice as fast as tortoise
        if torties == hare :    #if both meet then the duplicate element is found
            break
    ptr1=nums[0]    #set 2 pointers one to the start item and one more to the occurance duplicated item
    ptr2=torties
    while ptr1!=ptr2:   #travers till we get the begin of the cycle
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1 #return the duplicate element



#test case 

print(findDuplicates([1,2,3,4,2])) 