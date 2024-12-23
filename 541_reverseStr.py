# 541. Reverse String II

s = "abcdefg"
k = 2

# Loop through the string in steps of 2*k
for i in range(0, len(s), 2 * k):
    # Reverse the first k characters in the current 2*k block
    s = s[:i] + s[i:i+k][::-1] + s[i+k:]

# Print the modified string
print(s)



# NOTES:
# - The string is reversed in blocks of 2*k characters
# - The first k characters of each block are reversed
# - The string is updated in place