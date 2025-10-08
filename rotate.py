def rotate(arr, k):
    n = len(arr)
    k %= n
    return arr[-k:] + arr[:-k]

nums = [0,1,4,4,6,7]
rotated = rotate(nums, 4)
print(rotated)
