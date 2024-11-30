def binary_search(array,target):
    if not array or len(array)<1:
        return -1

    if len(array) == 1:
        return 0 if array[0] == target else -1

    mid = len(array) // 2
    print(f"Mid: {mid}")
    print(f"Mid value: {array[mid]}")

    if array[mid] == target:
        return mid

    if array[mid] > target:
        for i in range(0,mid):
            if array[i] == target:
                return i


    if array[mid] < target:
        for i in range(mid+1,len(array)):
            if array[i] == target:
                return i

    return -1

my_list = [1,2,3,4,5]

print(f"Binary search: {binary_search(my_list,2)}")

# Time complexity is O(n) because of for loop