# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Total_nodes = 0
        curr = head

        while curr:
            Total_nodes += 1
            curr = curr.next
        curr = head

        remove_index = Total_nodes - n
        if remove_index ==0:
            return head.next

        for i in range(Total_nodes-1):
            if (i+1) == remove_index:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head