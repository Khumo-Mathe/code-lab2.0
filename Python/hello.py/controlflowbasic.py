def two_sum(nums: list, target: int) -> list:
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value

        if complement in seen:
            return [seen[complement], index]

        seen[value] = index

    return []
# Example usage:
# print(two_sum([2, 7, 11, 15], 9))     # Output: [0, 1]
# print(two_sum([3, 2, 4], 6))          # Output


