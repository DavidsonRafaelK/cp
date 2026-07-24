class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        step = 0

        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num + 1
            step = step + 1

        return step

 
if __name__ == "__main__":
    sol = Solution()

    num = "1111011110000011100000110001011011110010111001010111110001"

    hasil = sol.numSteps(num)
    print(hasil)

