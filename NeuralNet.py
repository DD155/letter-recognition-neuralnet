import DataSet
import random
import math

tuple_size = 3
num_sets = math.floor(12 / tuple_size)  # amount of sets to be created depending on tuple size
r = []


def generate_index_set(index):
    """returns index_arr, array with random indices. uses tuple_size to get num_sets random indices (J)"""
    index_arr = []
    idx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for x in range(num_sets):
        random_points = []
        for y in range(tuple_size):  # gets random index from array, then removes index to have no duplicate indices
            rnd = idx[random.randint(0, (len(idx)-1))]
            random_points.append(rnd)
            idx.remove(rnd)
        index_arr.append(random_points)  # adds array of indices to index_arr

    return index_arr


def generate_rnd_set(index):
    """returns sets, an array that contains all values from data set that correspond to numbers in index set (S)"""
    indices = generate_index_set(index)
    sets_h = []
    sets_l = []
    sets = []
    for x in range(len(indices)):
        values = []
        for y in range(tuple_size):
            val = r[index][0][indices[x][y]-1]  # value of data set at index [x][y]. -1 b/c idx set is 1 to 12
            values.append(val)

        sets.append(values)

    return sets


def binary_conversion(binary_string):
    """ returns integer for the binary input (3-bit only)"""
    arr = list(binary_string)  # turns string into array

    return 4 * int(arr[0]) + 2 * int(arr[1]) + 1 * int(arr[2])


def convert_tuple_to_string(tpl):
    """Used for incrementation in training for binary string equivalent. Returns 3 bit binary string"""
    return "".join(str(tpl[0]) + str(tpl[1]) + str(tpl[2]))


def training():
    """Testing phase for neural network. Increments arrays depending on tuples for each data set."""
    class_h_arrays = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]  # 4 arrays in each class
    class_l_arrays = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

    #  training for H
    for x in range(200):
        tuples_h = generate_rnd_set(x)  # creates 2D array with all tuples from set H
        tuples_l = generate_rnd_set(300+x)  # creates 2D array with all tuples from set L
        for y in range(len(tuples_h)):  # creates second loop to iterate through the class_h_arrays
            class_h_arrays[y][binary_conversion(convert_tuple_to_string(tuples_h[y]))] += 1
            class_l_arrays[y][binary_conversion(convert_tuple_to_string(tuples_l[y]))] += 1
            # array at index y. gets from tuple sets, which is converted from binary to an integer as an index and ++
    '''
    for x in range(4):
        print(class_h_arrays[x])
    print("")
    for x in range(4):
        print(class_l_arrays[x])
    '''

    return [class_h_arrays, class_l_arrays]


def testing():
    """CPU must determine if the given image is an H or L depending on previous training data"""
    d = 0.2  # bonus
    results = training()
    ctr_h = 0; ctr_l = 0
    for x in range(200,300):  # last 100 arrays from each data set is now being tested
        sum_h = 0; sum_l = 0
        tuples_h = generate_rnd_set(x)
        for y in range(len(tuples_h)):  # creates second loop to iterate through the class_h_arrays
            sum_h += results[0][y][binary_conversion(convert_tuple_to_string(tuples_h[y]))]  # adds value @ index to sum
            sum_l += results[1][y][binary_conversion(convert_tuple_to_string(tuples_h[y]))]
        if sum_h > sum_l:
            guess = "H"
        else:
            guess = "L"
        if guess == r[x][1]:
            ctr_h += 1; g = "True"
            for y in range(len(tuples_h)):  # bonus
                results[0][y][binary_conversion(convert_tuple_to_string(tuples_h[y]))] += d  # adds dn value
        else:
            g = "False"
            for y in range(len(tuples_h)):  # bonus
                results[0][y][binary_conversion(convert_tuple_to_string(tuples_h[y]))] -= d  # subs dn value
        print(r[x][0], "Actual Class:", r[x][1], "Predicted Class:", guess, g)

    for x in range(500, 600):  # last 100 arrays from each data set is now being tested
        sum_h = 0; sum_l = 0
        tuples_l = generate_rnd_set(x)
        for y in range(len(tuples_h)):  # creates second loop to iterate through the class_h_arrays
            sum_h += results[0][y][binary_conversion(convert_tuple_to_string(tuples_l[y]))]  # adds value @ index to sum
            sum_l += results[1][y][binary_conversion(convert_tuple_to_string(tuples_l[y]))]
        if sum_h > sum_l:
            guess = "H"
        else:
            guess = "L"
        if guess == r[x][1]:
            ctr_h += 1; g = "True"
            for y in range(len(tuples_h)):  # bonus
                results[1][y][binary_conversion(convert_tuple_to_string(tuples_h[y]))] += d
        else:
            g = "False"
            for y in range(len(tuples_h)):  # bonus
                results[1][y][binary_conversion(convert_tuple_to_string(tuples_h[y]))] -= d
        print(r[x][0], "Actual Class:", r[x][1], "Predicted Class:", guess, g)
    print((((ctr_l+ctr_h)/200)*100), "% accuracy", ":",ctr_l+ctr_h, "/ 200")
        #print(r[x][0], "Actual Class:", r[x][1], "Predicted Class: ", guess)


def main():
    # creates r, the data sets generated previously
    for x in range(len(DataSet.dataSetH())):
        r.append(DataSet.dataSetH()[x])
    for x in range(len(DataSet.dataSetL())):
        r.append(DataSet.dataSetL()[x])

    testing()
    for x in range(len(r)): print(r[x][0])

main()
