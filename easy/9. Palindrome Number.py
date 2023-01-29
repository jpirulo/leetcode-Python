class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_word = "".join(reversed(str(x)))
        if reversed_word == str(x):
            return True
        else:
            return False
