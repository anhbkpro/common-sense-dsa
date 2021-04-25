from typing import List


def singleNumber(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    result = {}
    for num in nums:
        if num in result and result[num]:
            del result[num]
            continue

        result[num] = True

    return list(result.keys())[0]


print(singleNumber([4, 1, 2, 1, 2]))
