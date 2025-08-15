def twoSum(self, nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Get input as a list of integers from the user
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the target number: "))
result = twoSum(None, nums, target)
print("Indices of the two numbers that add up to the target:", result)