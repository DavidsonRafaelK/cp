class Solution:
    def minPartitions(self, n: str) -> int:
       return int(max(n))


if __name__ == "__main__":
    sol = Solution()

    n = "27346209830709182346"
    print(sol.minPartitions(n))
