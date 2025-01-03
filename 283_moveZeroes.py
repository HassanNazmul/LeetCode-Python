# 283. Move Zeroes


# Using sort function
def moveZeroes(nums):
    nums.sort(key=lambda x: x == 0) # sort based on the boolean value of x == 0

# Using remove() and append():

def moveZeroes2(nums):
    for i in range(nums.count(0)): # count the number of 0s in the list
        nums.remove(0)  # remove the 0s from the list
        nums.append(0)  # append the 0s at the end of the list


# NOTES:
    # The sort() method sorts the list ascending by default.
    # The `lambda x: x == 0` part:
    #    - This is a lambda function (a small anonymous function)
    #    - For each element `x` in the list, it returns:
    #      - `True` if x is 0
    #      - `False` if x is not 0
    #    - In Python, `False` comes before `True` when sorting
