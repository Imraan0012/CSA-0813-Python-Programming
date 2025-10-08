
arr = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3

arr.sort()

nth_min = arr[N - 1]
mth_max = arr[-M]

sum_val = nth_min + mth_max
diff_val = abs(mth_max - nth_min)

print(f"{M}st Maximum Number = {mth_max}")
print(f"{N}rd Minimum Number = {nth_min}")
print("Sum =", sum_val)
print("Difference =", diff_val)
