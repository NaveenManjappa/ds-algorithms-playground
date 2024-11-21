iteration =0
def merge_sort(array):
   
    global iteration
    iteration+=1
    print(f"Merge Sort iteration:{iteration} : {array}")

    if(len(array)) <= 1:
        return array

    middle_index = (len(array)-1) // 2
    print(f"Middle Index: {middle_index}")

    # right = array[:middle_index]
    # left = array[middle_index:]
    # print(f"Right: { right }")
    # print(f"Left: { left }")

    left = array[:middle_index+1]
    right = array[middle_index+1:]
    print(f"Left: {left}")
    print(f"Right: {right}")


    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left,sorted_right)

def merge(left,right):
        results = []

        left_index =0
        right_index= 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                results.append(left[left_index])
                left_index += 1
            else:
                results.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            results.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            results.append(right[right_index])
            right_index += 1


        return results





my_list = [5, 2, 9,1,7,6]
print(merge_sort(my_list))

my_list2= [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(my_list2))