def binary_search(array,target):
    if len(array) < 1:
        return -1

    left,right = 0,len(array)-1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid -1
        else:
            left = mid + 1

    return -1

my_list = [1,2,3,4,5]

print(f"Binary search: {binary_search(my_list,22)}")

# Time complexity: O(n)
# Space complexity: O(1)