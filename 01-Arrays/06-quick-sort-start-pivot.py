def quick_sort(array,start,end):

    if start >= end:
        return

    pivot_index = partition(array,start,end)

    quick_sort(array,start,pivot_index-1)
    quick_sort(array,pivot_index+1,end)


def partition(array,start,end):
    pivot = array[start]
    i = start

    for j in range(start+1,end+1):
        if array[j] <= pivot:
            i += 1
            if j !=i:
                array[i],array[j] = array[j],array[i]

    pivot_index = i

    if pivot_index != start:
        array[pivot_index],array[start] = array[start],array[pivot_index]

    return pivot_index

my_list = [2,1,8,4,5,0,0]

quick_sort(my_list,0,len(my_list)-1)
print(f"Sorted array: {my_list}")