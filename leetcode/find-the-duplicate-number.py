from typing import List


def findDuplicate(nums: List[int]) -> int:
    """
    Testcase
    [1, 3, 4, 2, 2]
    [3, 1, 3, 4, 2]
    [1, 1]
    [1, 1, 2]
    """
    hashes = {}
    for num in nums:
        if num in hashes:
            return num
        hashes[num] = True


class Solution:
    pass






