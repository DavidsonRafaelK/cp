class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        numbers = sorted(nums)
        a = numbers[-1] * numbers[-2] * numbers[-3]
        b = numbers[0] * numbers[1] * numbers[-1]
    
        return max(a, b)

if __name__ == "__main__": 
    sol = Solution()
    nums = [-100, -98, 1, 2, 3, 4] 
    print(sol.maximumProduct(nums)) 
