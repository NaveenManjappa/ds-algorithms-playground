def quick_sort(array,start,end):
    print(f"Quick sort array: {array}")
    if start >= end:
        return

    pivot_index = partition(array,start,end)
    print(f"Pivot index: {pivot_index}")

    quick_sort(array,start,pivot_index-1)
    quick_sort(array,pivot_index+1,end)

def partition(array,start,end):
    pivot = array[end]
    smaller_index = start-1
    print(f"Partition array: {array}, start: {start}, end:{end}")
    for current in range(start,end,1):
        print(f"Current: {current}")
        if array[current] <= pivot:
            smaller_index +=1
            if smaller_index != current:
                temp = array[smaller_index]
                array[smaller_index] = array[current]
                array[current] = temp


    pivot_index = smaller_index + 1

    if pivot_index != end:
        temp = array[pivot_index]
        array[pivot_index] = array[end]
        array[end] = temp
    print(f"After partition: {array}")
    return pivot_index

my_list=  [2,3,1]

quick_sort(my_list,0,len(my_list)-1)

print(my_list)