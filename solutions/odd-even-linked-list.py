# Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        oddlist = []
        evenlist = []
        curr = head
        count = 0
        while curr != None:
            if count%2 == 0:
                oddlist.append(curr.val)
            else:
                evenlist.append(curr.val)
            count += 1
            curr = curr.next
        print(oddlist)
        print(evenlist)
        new_head = ListNode(oddlist[0])
        newcurr = new_head

        for i in range(1, len(oddlist)):
            newcurr.next = ListNode(oddlist[i])
            newcurr = newcurr.next
        for i in range(0, len(evenlist)):
            newcurr.next = ListNode(evenlist[i])
            newcurr = newcurr.next
        print(new_head)
        return new_head
