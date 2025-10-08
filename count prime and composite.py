numbers = [4, 54, 29, 71, 59, 98, 23]

prime_count = 0
composite_count = 0

for num in numbers:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composite_count += 1
                break
        else:
            prime_count += 1

print("Composite numbers =", composite_count)
print("Prime numbers =", prime_count)
