from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        trailing_zeros = []
        for row in grid:
            count = 0
            for val in reversed(row):   
                if val == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        total_swaps = 0
        for i in range(n):
            required = n - i - 1
            
            found = -1
            for j in range(i, n):
                if trailing_zeros[j] >= required:
                    found = j
                    break
            
            if found == -1:
                return -1
            
            total_swaps += (found - i)
            
            value = trailing_zeros.pop(found)
            trailing_zeros.insert(i, value)
        
        return total_swaps

if __name__ == "__main__":
    sol = Solution()
    grid = [[0,0,1],[1,1,0],[1,0,0]]
    print(sol.minSwaps(grid))
