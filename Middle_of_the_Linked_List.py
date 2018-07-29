# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        tmp_h = head
        mid = head

        while tmp_h != None:

            i = i + 1
            tmp_h = tmp_h.next

            if i % 2 == 0:
                mid = mid.next

        return mid
        

if __name__ == "__main__":

    a = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)

    n1.next = n2
    n2.next = n3

    x = a.middleNode(n1)

    print(x.val)