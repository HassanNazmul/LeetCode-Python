# 557. Reverse Words in a String III

s = "Let's take LeetCode contest"

# Split the string into words
words = s.split()   # Split each word into a list of characters

# Reverse each word
for i in range(len(words)): # For each word in the list
    words[i] = words[i][::-1]   # Reverse the word

# Join the words back together
s = ' '.join(words) # Join the words back together with a space in between

print(s)



# NOTES:
# The split() method splits a string into a list where each word is a list item.
# The join() method joins the elements of an iterable to the end of the string.