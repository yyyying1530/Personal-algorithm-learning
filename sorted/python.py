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

if __name__ == "__main__":
    a = [15,2,32,45,6,9]
    print(bubble_sort(a))