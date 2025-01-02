# 66. Plus One

def plusOne(digits):
    n = len(digits) - 1     # Get index of last digit
    while n >= 0:           # Work from right to left
        if digits[n] < 9:   # If current digit is less than 9
            digits[n] += 1  # Increment it by 1
            return digits   # Return the modified array
        digits[n] = 0       # Set digit to 0 if it was 9
        n -= 1              # Move to next digit to the left
    digits.insert(0, 1)     # Insert 1 at beginning if all digits were 9
    return digits           # Return the modified array



# NOTES:
    # # To solve this problem, follow these steps:# 1) Start from the rightmost digit
        # 1. If the digit is less than 9, increment it and return the array
        # 2. If the digit is 9, set it to 0 and move to the next digit
        # 3. After all digits are processed, if every digit was 9, we need to add 1 at the front

    # # Built-in Functions:
        # len() returns the number of items in an object
        # .insert() adds an element at the specified position
