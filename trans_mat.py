

class Solution:

    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        R = len(A)
        C = len(A[0])

        result = []

        for r in range(C):
            row = []
            for c in range(R):
                row.append(A[c][r])
            result.append(row)
        
        return result


if __name__ == "__main__":

    M = [[1,2,3],[4,5,6],[7,8,9]]

    a = Solution()
    ans = a.transpose(M)

    print(ans)

