def is_prime_using_while(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False

    # Start checking from 2, since 1 is not a valid divisor for prime checking
    i = 2

   
    # This is because a larger factor must be a multiple of a smaller factor
    while i * i <= num:
        # If num is divisible by i, it is not a prime number
        if num % i == 0:
            return False
        i += 1  # Increment i by 1 for the next iteration

    # If no divisors are found, num is a prime number
    return True

# Example usage
number = 29
if is_prime_using_while(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
