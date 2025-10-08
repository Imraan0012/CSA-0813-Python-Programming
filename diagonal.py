a = [1,2,3,4,5,6,7,8,9]
n = 3
s = 0
print("Diagonal elements are:", end=" ")
for i in range(n):
    print(a[i*n + i], end=" ")
    s += a[i*n + i]
print("\nSum of diagonal elements =", s)
