def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        minindex = i
        for j in range(i + 1, n):
            if nums[minindex] > nums[j]:
                minindex = j
        nums[i], nums[minindex] = nums[minindex], nums[i]
    return nums

def bubble_sort(nums):
    n = len(nums)
    flag = True
    while flag:
        flag = False
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                 flag = True
                 nums[i + 1], nums[i] = nums[i], nums[i + 1]
    return nums

def insertion_sort(nums):
    n = len(nums)
    for i in range(1,n):
        x = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > x:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = x
    return nums

def counting_sort(nums):
    W = max(nums) + 1
    n = len(nums)
    w = [0] * W
    ans = [0] * n
    for i in nums:
        w[i] += 1
    for i in range(1, W):
        w[i] += w[i-1]
    for i in nums:
        ans[w[i] - 1] = i
        w[i] -= 1
    return ans


if __name__ == "__main__":
    a = [15,2,32,45,6,9]
    print(counting_sort(a))