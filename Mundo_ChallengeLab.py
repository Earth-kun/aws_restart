def is_prime(num):
    """Check if a number is prime."""
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 250
primes = [str(i) for i in range(1, n + 1) if is_prime(i)]

with open("results.txt", "w") as file:
    file.write("\n".join(primes))
print("Prime numbers from 1 to 250 have been written to results.txt.")

