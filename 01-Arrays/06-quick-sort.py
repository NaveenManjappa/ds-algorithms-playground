partition_count = 1
quick_sort_count =1
def quick_sort(array,start,end):
    global quick_sort_count
    print(f"Quick sort count: {quick_sort_count}")
    quick_sort_count += 1
    print(f"Quick sort array: {array}, start: {start}, end: {end}")

    if start >= end:
        return

    pivot_index = partition(array,start,end)
    print(f"Pivot index: {pivot_index}")

    quick_sort(array,start,pivot_index-1)
    quick_sort(array,pivot_index+1,end)

    print(f"Return from Quick sort: {quick_sort_count}")


def partition(array,start,end):
    global partition_count
    print(f"Partition count: {partition_count}")
    pivot = array[end]
    print(f"Pivot: {pivot}")
    smaller_index = start-1
    print(f"Partition array: {array}, start: {start}, end:{end}")

    for current in range(start,end,1):
        print(f"Iteration: {current + 1}")
        print(f"Current: {current}")
        if array[current] <= pivot:
            print(f"Current element is < pivot: {array[current]} < {pivot}")
            smaller_index +=1
            print(f"Smaller index: {smaller_index}")
            if smaller_index != current:
                temp = array[smaller_index]
                array[smaller_index] = array[current]
                array[current] = temp
                print(f"Array after swap: {array}")

    print(f"After for loop: {array}")
    pivot_index = smaller_index + 1

    if pivot_index != end:
        temp = array[pivot_index]
        array[pivot_index] = array[end]
        array[end] = temp
    print(f"After partition: {array}")

    partition_count += 1
    return pivot_index

my_list=  [2,4,1,3]

quick_sort(my_list,0,len(my_list)-1)

print(my_list)