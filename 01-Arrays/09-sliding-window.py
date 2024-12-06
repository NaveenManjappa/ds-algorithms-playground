def find_maximum(array,window_size):
    if window_size <=0:
        return []

    max =[]
    for i in range(len(array)-window_size+1):
        print(f"i: {i}")
        max_val = array[i]
        for j in range(i,i + window_size):
            print(f"j: {j}")
            if i + window_size > len(array):
                break
            if array[j] > max_val:
                max_val = array[j]
            print(f"Max: {max_val}")
        max.append(max_val)
        print(max)

    return max

my_list = [0,1,3]

print(f"Result: {find_maximum(my_list,2)}")

#Time complexity: O(n^2)