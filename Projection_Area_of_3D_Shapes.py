class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ans = 0
        for i in range(len(grid)):
            tmp = 0
            tmp2 = 0
            tmp3 = 0
            for j in range(len(grid)):
                if grid[i][j] > tmp:
                    tmp = grid[i][j]
                if grid[j][i] > tmp2:
                    tmp2 = grid[j][i]
                if grid[i][j] > 0:
                    tmp3 += 1
            ans += tmp
            ans += tmp2
            ans += tmp3

        return ans

if __name__ == "__main__":

    a = Solution()

    #ans = a.projectionArea([[1,1,1],[1,0,1],[1,1,1]])
    ans = a.projectionArea([[2,2,2],[2,1,2],[2,2,2]])

    print(ans)
