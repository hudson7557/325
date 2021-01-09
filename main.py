# CS 325
# Homework 1
# Scott Hudson

# Function which takes an open file as an argument and returns a cleaned array
# containing all the numbers in the file.
def create_array(nums):
    unsorted_array = []

    line = nums.readline().strip()

    while line != '':

        current_line = line.split(' ')

        for i in range(len(current_line)):

            # have to get around the annoying first number that says how many
            # numbers are in the line.
            if i != 0:
                unsorted_array.append(current_line[i])

        line = nums.readline().strip()

    return unsorted_array


def merge(a, b):
    index_a = 0
    index_b = 0
    c = []
    while index_a < len(a) and index_b < len(b):
        if a[index_a] <= b[index_b]:
            c.append(a[index_a])
            index_a = index_a + 1
        else:
            c.append(b[index_b])
            index_b = index_b + 1
    # when we exit the loop
    # we are at the end of at least one of the lists
    c.extend(a[index_a:])
    c.extend(b[index_b:])
    return c


def msort(list):
    if len(list) == 0 or len(list) == 1:  # base case
        return list[:len(list)]  # copy the input
    # recursive case
    halfway = len(list) // 2
    list1 = list[0:halfway]
    list2 = list[halfway:len(list)]
    newlist1 = msort(list1)  # recursively sort left half
    newlist2 = msort(list2)  # recursively sort right half
    newlist = merge(newlist1, newlist2)
    return newlist


def insertion_sort():
    return


if __name__ == '__main__':
    file = open('data.txt')
    array = create_array(file)
    file.close()
    print(array)
    sorted_array = msort(array)
    print(sorted_array)
