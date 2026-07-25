class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        temp = n
        while temp > 0:
            digit = temp % 10
            digits.append(digit)
            temp = temp // 10

        max_product = 0
        for i in range(len(digits)):
            for j in range(i+1, len(digits)):
                product = digits[i] * digits[j]
                if product > max_product:
                    max_product = product
        return max_product

if __name__ == "__main__":
    sol = Solution()
    
    n = 124
    print(sol.maxProduct(n))
