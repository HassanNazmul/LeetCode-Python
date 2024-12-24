# 13. Roman to Integer

s = 'LVIII'

roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

total = 0   # Sum of all the values
last_value = 0  # Last value that was added to the total

for i in reversed(s):  # Reversing the string
    current_valuse = roman_dict[i]  # Getting the value of the current roman numeral

    if current_valuse < last_value: # If the current value is less than the last value, then we need to subtract the current value from the total
        total -= current_valuse # Subtracting the current value from the total

    else:
        total += current_valuse # Adding the current value to the total

    last_value = current_valuse # Updating the last value

print(total)