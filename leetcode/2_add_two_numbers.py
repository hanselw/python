
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        carry = 0
        head = ListNode(0)
        cur = head
        while l1 != None or l2 != None :
            la = l1.val if l1 != None else 0
            lb = l2.val if l2 != None else 0 
            sum = la + lb + carry
            carry = sum / 10
            cur.next = ListNode(sum%10)
            cur = cur.next
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            
        if carry > 0 :
            cur.next = ListNode(carry)
            
        return head.next