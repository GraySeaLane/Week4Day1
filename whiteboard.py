# Move Zeros
# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example Input: [0,0,11,2,3,4]
# Example Output: [11,2,3,4,0,0]

# Example Input: [0,5,0,0,3]
# Example Output: [5,3,0,0,0]

def my_list(nums):
    for num in nums:
        if num == 0:
            nums.append(num)
            nums.remove(num)
    return nums

print(my_list([0,1, 0, 3, 12]))
