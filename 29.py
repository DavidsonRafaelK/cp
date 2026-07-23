class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        remaining = dividend
        result = 0

        while remaining >= divisor:
            temp = divisor
            multiple = 1

            while temp << 1 <= remaining:
                temp = temp << 1
                multiple = multiple << 1

            remaining -= temp
            result = result + multiple
    
        if negative:
            result = -result
        
        return max(INT_MIN, min(INT_MAX, result))

if __name__ == "__main__":
    sol = Solution()

    a = -2147483648
    b = -1
    c = 7
    d = -3

    hasil = sol.divide(a, b)
    hasil2 = sol.divide(c, d)

    print(f"Input 1: {(a, b)}")
    print(f"Input 2: {(c, d)}")
    print(f"Output 1: {hasil}")
    print(f"Output 2: {hasil2}")
