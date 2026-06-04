# DSA Problem 1: Two Sum
# Goal: Return the indexes of two numbers that add up to the target.

nums = [2, 7, 11, 15]
target = int(input("Enter your target value: "))


# My first solution: brute force
def two_sum_brute_force(nums, target):
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# Better solution: dictionary / hashmap
def two_sum_hashmap(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    return []


print("Brute force answer:", two_sum_brute_force(nums, target))
print("Hashmap answer:", two_sum_hashmap(nums, target))