def binary_search(array,search_el):
    print(f"Binary search: {array} {search_el}")
    element_found = False

    if len(array) <1:
        element_found = False
        return False

    if len(array) == 1:
        if search_el == array[0]:
            print("this is true")
            element_found = True
            return True
        else:
            element_found = False
            return False

    middle_index = len(array) // 2
    print(f"Middle index: {middle_index}")

    if search_el == array [middle_index]:
        element_found = True
        return True

    if search_el > array[middle_index]:
        element_found=binary_search(array[middle_index+1:],search_el)

    if search_el < array[middle_index]:
        element_found = binary_search(array[:middle_index],search_el)

    return element_found


my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
is_found = binary_search(my_list,231)
print(f"Element found: {is_found}")