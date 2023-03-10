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
