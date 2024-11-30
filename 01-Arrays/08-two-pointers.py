# This is the implementation of two pointers technique to remove the duplicates
def remove_duplicates(array):

    if len(array) <=1:
       return len(array)

    reader_pointer = 1
    writer_pointer = 0

    #print(f"Array length: {len(array)}")
    while reader_pointer < len(array):
        #print(f"Writer pointer: {writer_pointer}")
        #print(f"Reader pointer: {reader_pointer}")
        if array[reader_pointer] != array[writer_pointer]:
            #print(f"Incrementing writer")
            writer_pointer += 1
            array[writer_pointer] = array[reader_pointer]

        reader_pointer += 1



    print(array)
    return writer_pointer +1

my_list = [1,2,2,3,3,4,4,4,4,4]
print(f"Result: { my_list[:remove_duplicates(my_list)]}")


