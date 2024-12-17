# 204. Count Primes

def countPrimes(n):
    n = 10
    primes = 0

    for i in range(2, n):
        is_prime = True

        for j in range(2, int(i ** 0.5) + 1): 
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            primes += 1

    return primes


# THIS PROBLEMS HAH ISSUES WITH THE TIME LIMIT

# Alternate Solution
def countPrimes(n):

    if n <= 2:  # No primes less than 2
        return 0
    
    is_prime = [True] * n  # Assume all numbers < n are prime
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    for i in range(2, int(n ** 0.5) + 1):  # Start checking from 2
        if is_prime[i]:
            # Mark multiples of i as not prime
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    # Count the True values remaining in the list
    return sum(is_prime)



# NOTES:
# - Created a variable to store the number of primes
# - Iterated through the range of 2 to n
# - Created a variable to store whether the number is prime
# - Iterated through the range of 2 to the square root of i + 1
# - Checked if i is divisible by j
# - Incremented the primes variable if i is prime