# Find Numbers with Even Number of Digits

nums = [12,345,2,6,7896]
digit_counts = []
even_nums = 0

for number in nums:
    digit_count = len(str(number))
    digit_counts.append(digit_count)

for i in digit_counts:
    if i % 2 == 0:
        even_nums += 1

print(even_nums)

# OPTIMIZED SOLUTION
def findNumbers(nums):
    return sum(1 for num in nums if len(str(num)) % 2 == 0)

print(findNumbers([12,345,2,6,7896]))



# Notes:
# - Created a list to store the number of digits in each number in the list
# - Created a variable to store the count of even numbers
# - Iterated through the list of digit counts and checked if the count was even
# - Incremented the even_nums variable if the count was even

# Optimized Solution:
# - Used a generator to iterate through the list of numbers and checked if the number of digits was even