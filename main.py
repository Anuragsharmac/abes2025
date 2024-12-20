def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def custom_sort(arr):
    primes = [x for x in arr if is_prime(x)]
    non_primes = [x for x in arr if not is_prime(x)]
    
    if not primes:
        return sorted(arr, reverse=True)
    
    prime1 = max(primes)
    prime2 = min(primes)
    
    primes.remove(prime1)
    primes.remove(prime2)
    
    sorted_arr = [prime1] + sorted(non_primes + primes, reverse=True) + [prime2]
    return sorted_arr


print(custom_sort([5, 1, 8, 11, 2]))
print(custom_sort([1, 6, 4, 13, 9, 3]))  
