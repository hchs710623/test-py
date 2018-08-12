class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        listA = A.split()
        listB = B.split()

        listAB = listA + listB

        ans = []
        for element in listAB:
            if listAB.count(element) == 1:
                ans.append(element)

        return ans

if __name__ == "__main__":

    # A = "this apple is sweet"
    # B = "this apple is sour"
    # A = "apple apple"
    # B = "banana"
    A = "s z z z s"
    B = "s z ejt"
    
    a = Solution()
    
    ans = a.uncommonFromSentences(A, B)

    print(ans)