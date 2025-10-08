arr = list(map(int, input("Enter elements: ").split()))
arr.sort()
print("Largest two elements:", arr[-2], "&", arr[-1])
