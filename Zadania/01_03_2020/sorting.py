def bubble_sort(list_of_numbers):
    temp_list = list_of_numbers
    for number in temp_list:
        for i in range(0, len(temp_list) - 1):
            if temp_list[i] > temp_list[i+1]:
                temp_list[i], temp_list[i+1] = temp_list[i+1], temp_list[i]
    return temp_list

def insertion_sort(list_of_numbers):
    temp_list = list_of_numbers
    for i in range(1, len(list_of_numbers)):
        compared_number = temp_list[i]
        counter = i - 1
        while counter >= 0 and compared_number < temp_list[counter]:
            temp_list[counter + 1] = temp_list[counter]
            counter -= 1
        temp_list[counter + 1] = compared_number
    return temp_list

list_to_sort = [30, 43, 87, 62, 28, 95, 66, 3, 74, 85, 18, 67, 46, 15, 38, 93, 68, 57, 19, 13, 10, 91, 33, 29, 20, 92, 40, 23, 9, 44, 14, 41, 71, 4, 70, 84, 11, 48, 76, 42, 52, 8, 53, 26, 61, 99, 77, 32, 45, 21, 16, 25, 49, 80, 35]

print(list_to_sort)
print(insertion_sort(list_to_sort))
print(bubble_sort(list_to_sort))
