class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def gkey(n):
            s = bin(n).count('1')
            return (s, n)

        arr.sort(key=gkey)
        return arr

    # atau cara simpel pake lambda function
    # arr.sort(key=lambda n: (bin(n).count('1'), n))
    # return arr

if __name__ == "__main__":
    sol = Solution()
    
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    print(f"Input: {arr}")

    hasil = sol.sortByBits(arr)
    print(f"Output: {hasil}")
