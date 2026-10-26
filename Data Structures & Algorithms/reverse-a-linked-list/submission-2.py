# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        "0-> 1 -> 2 -> 3"
        "NONE <- 0,  <- 1 <- 2 <- 3"

        dummy = None
        current = head 

        while current:
            prev = current
            current = current.next
            prev.next = dummy 
            dummy = prev
    
       
            
            
        
        return dummy