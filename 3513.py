from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        else:
            return 2 ** len(nums).bit_length()

if __name__ == "__main__":
    sol = Solution()
    
    test_nums = [1, 2, 3, 4]
    
    hasil = sol.uniqueXorTriplets(test_nums)
    
    print(f"Input: {test_nums}")
    print(f"Output: {hasil}")
