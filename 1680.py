class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            s = i.bit_length()
            res = (res << s) + i
            res = (res % (10**9 + 7))
        return res

        # mod = 10**9 + 7 # constraint soal
        # tmp = ""
        # for i in range(1, n + 1):
        #     tmp += bin(i)[2:]
        # tmp = int(tmp, 2)
        # res = tmp % mod
        # return res

        # tmp = []
        # for i in range(1, n + 1):
        #     tmp.append(bin(i)[2:])
        # s = "".join(tmp)
        # return int(s, 2)

if __name__ == "__main__":
    sol = Solution()
    
    n = 12
    print(sol.concatenatedBinary(n))
