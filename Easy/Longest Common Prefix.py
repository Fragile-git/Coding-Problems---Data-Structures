

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.




short = min(strs, key=len) # Get the shortest word since we are only comparing the common prefix
prefix = short
for s in strs:
    for i in range(len(prefix)):
        if(s[i] != prefix[i]):
            prefix=prefix[:i] # Slice the shortest word until the common prefix
            break # stop the loop, check other elements 
return prefix