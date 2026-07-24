class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        dp = {0} 

        for _ in range(3):
            tmp = set()
            for x in nums:
                for v in dp:
                    tmp.add(x ^ v)
            dp = tmp
        return len(dp)

if __name__ == "__main__":
    sol = Solution()
    
    nums = [6,7,8,9]
    hasil = sol.uniqueXorTriplets(nums)
    print(hasil)
