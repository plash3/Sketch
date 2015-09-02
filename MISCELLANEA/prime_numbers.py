prime_nums = []
num = 2
while num <= 23:
    is_prime = True
    trial = 2
    while trial**2 <= num:
        if (num % trial) == 0:
            is_prime = False
            break
        trial += 1
    if is_prime:
        prime_nums.append(num)
    num += 1
print prime_nums
