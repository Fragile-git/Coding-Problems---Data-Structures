# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

s ="III"

roman = {
            'I':1, "V":5 , "X":10, "L":50, "C":100, "D":500, "M": 1000
}

result = 0

for index in range(0, len(s)):
    if index+1< len(s) and roman[s[index]] < roman[s[index+1]]: # if next element is larger or there is no element left 
        result -= roman[s[index]] # Subtract
    else:
        result += roman[s[index]] # Add
        
print(result)


# Reverse Method: 
# Start comparing from to smallest to largest 
# If previous element is larger ; subtract 

result_number = 0 # Total 
previous_number = 0 # Used to compare

for symbol in s[::-1]:  # Reverse the roman to compare from smallest to largest
    if roman[symbol] >=previous_number: # previous number is smaller
        result_number += roman[symbol]
    else:
        result_number -= roman[symbol] # previous number is larger so subtract
    previous_number = roman[symbol]

print(result_number)



