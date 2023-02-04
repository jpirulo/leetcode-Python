# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lista = []
        current = head
        while current is not None:
            lista.append(current.val)
            current = current.next
        for i in range(len(lista) // 2):
            if lista[i] != lista[-i - 1]:
                return False
        return True
