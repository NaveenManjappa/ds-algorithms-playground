def quick_sort(array, start, end):

    #Base case
    if start >= end:
        return

    pivot_index = partition(array,start,end)

    quick_sort(array,start,pivot_index-1)
    quick_sort(array,pivot_index+1,end)



def partition(array,start,end):
    i = start-1
    j = start
    pivot = array[end]

    for j in range(start,end,1):
        if array[j] < pivot:
            i += 1
            if i !=j:
                array[i], array[j] = array[j], array[i]
        j += 1

    pivot_index = i + 1

    if pivot_index != end:
        array[pivot_index],array[end] = array[end],array[pivot_index]

    return pivot_index


my_list = [2,1,8,4,5]

quick_sort(my_list,0,len(my_list)-1)
print(f"Sorted array: {my_list}")