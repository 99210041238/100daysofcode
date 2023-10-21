class Solution:
    def intToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        roman_numeral = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_numeral += syms[i]
                num -= val[i]
            i += 1
        return roman_numeral

# Example usage:
converter =Solution()
print(converter.intToRoman(3))    # Output: "III"
print(converter.intToRoman(58))   # Output: "LVIII"
print(converter.intToRoman(1994)) # Output: "MCMXCIV"
