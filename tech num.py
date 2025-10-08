n = 2025
num_str = str(n)
d = len(num_str) // 2
first_half = int(num_str[:d])
second_half = int(num_str[d:])
print((first_half + second_half) ** 2 == n)
