class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # S1 = 0
        # S2 = S2 - 1 + "1" + reverse(invert(S2 - 1))
        # S2 = 0 - 1 + "1" + reverse(invert(0))
        # S2 = 011
        # S3 = 011 - 1 + "1" + reverse(invert(011))
        # S3 = 0111001
        # S4 = 0111001 - 1 + "1" + reverse(invert(0111001))
        # S4 = 011100110110001
        # Sn = Sn - 1 + "1" + reverse(invert(Sn))
        # S20 = S19 - 1 + "1" + reverse(invert(S19))
        
        # mirror = length - k + 1
        def solve(n, k):
            if n == 1:
                return '0' # base case
            length = 2**n - 1
            mid = (length + 1) // 2

            if k == mid:
                return '1' # mid position
            elif k < mid:
                return solve(n - 1, k) # position left sama kayak S(n-1)
            else:
                mirror = length - k + 1
                res = solve(n - 1, mirror)
                if res == '0': # invert
                    return '1'
                else:
                    return '0'

        return solve(n, k)

if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 11

    print(sol.findKthBit(n, k))
