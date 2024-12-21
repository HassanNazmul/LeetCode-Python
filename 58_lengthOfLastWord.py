# 58. Length of Last Word

s = "fly me to the moon  "

s = s.strip().split()[-1]   # Remove white space, split the string and get the last word
print(len(s))            # Return the length of the last word



# NOTES:
# - strip() removes white space from the beginning and end of the string
# - split() splits the string into a list of words
# - [-1] gets the last word from the list
# - len() returns the length of the string