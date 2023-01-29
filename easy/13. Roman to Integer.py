class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        previous = 0
        for letter in reversed(s):
            if letter not in roman:
                return 0
            if roman[letter] < previous:
                sum -= roman[letter]
            else:
                sum += roman[letter]
            previous = roman[letter]
        return sum
