# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        temp1 = head1
        temp2 = head2

        result = ListNode(-1)
        temp_result = result

        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp_result.next = temp1
                temp1 = temp1.next
            else:
                temp_result.next = temp2
                temp2 = temp2.next
            
            temp_result = temp_result.next


        while temp1:
            temp_result.next = temp1
            temp_result = temp_result.next
            temp1 = temp1.next

        while temp2:
            temp_result.next = temp2
            temp_result = temp_result.next
            temp2 = temp2.next


        result = result.next
        return result
        