iteration =0
def merge_sort(array):
   
    global iteration
    iteration+=1
    print(f"Merge Sort iteration:{iteration} : {array}")

    # Base case: if array has 1 or fewer elements, it's already sorted
    if(len(array)) <= 1:
        return array

    middle_index = len(array) // 2
    print(f"Middle Index: {middle_index}")

    # Split array into two halves
    left = array[:middle_index]
    right = array[middle_index:]
    print(f"Left: {left}")
    print(f"Right: {right}")

    # Recursively sort both halves
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    print(f"Sorted Left: {sorted_left}")
    print(f"Sorted Right: {sorted_right}")

    # Merge the sorted halves
    return merge(sorted_left,sorted_right)

def merge(left,right):
        print("Merge: ")
        results = []

        left_index =0
        right_index= 0

        # Compare elements from both arrays and merge them in sorted order
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                results.append(left[left_index])
                left_index += 1
            else:
                results.append(right[right_index])
                right_index += 1

        # while left_index < len(left):
        #     results.append(left[left_index])
        #     left_index += 1
        #
        # while right_index < len(right):
        #     results.append(right[right_index])
        #     right_index += 1

        # Add remaining elements from left array, if any
        results.extend(left[left_index:])

        # Add remaining elements from right array, if any
        results.extend(right[right_index:])

        print(f"Results: {results}")
        return results


my_list = [64, 34, 34,25, 12, 22, 11, 90]
print(merge_sort(my_list))
