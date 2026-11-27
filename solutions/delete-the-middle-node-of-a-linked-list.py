# Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            head = None
            return head
        count = 0
        curr = head
        while curr != None:
            count+=1
            curr = curr.next
        stop = count//2
        
        new_head = ListNode(head.val)
        oldcurr = head.next
        newcurr = new_head
        count1 = 0
        while oldcurr:
            count1+=1
            if count1 != stop:
                newcurr.next = ListNode(oldcurr.val)
                oldcurr = oldcurr.next
                newcurr = newcurr.next
            else:
                oldcurr = oldcurr.next
        return new_head
