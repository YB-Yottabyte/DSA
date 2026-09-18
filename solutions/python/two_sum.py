def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    raise ValueError("No valid two-sum pair found")
