import DataSet
import random
import math

tuple_size = 3
num_sets = math.floor(12 / tuple_size)  # amount of sets to be created depending on tuple size
r_h = []
r_l = []


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
        values_h = []
        values_l = []
        for y in range(tuple_size):
            val_h = r_h[index][0][indices[x][y]-1]  # value of data set at index [x][y]. -1 b/c idx set is 1 to 12
            val_l = r_l[index][0][indices[x][y]-1]
            values_h.append(val_h)
            values_l.append(val_l)

        sets_h.append(values_h); sets.append(sets_h)
        sets_l.append(values_l); sets.append(sets_l)

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
        tuples_h = generate_rnd_set(x)[0]  # creates 2D array with all tuples from set H
        tuples_l = generate_rnd_set(x)[1]  # creates 2D array with all tuples from set L
        for y in range(len(tuples_h)):  # creates second loop to iterate through the class_h_arrays
            class_h_arrays[y][binary_conversion(convert_tuple_to_string(tuples_h[y]))] += 1
            class_l_arrays[y][binary_conversion(convert_tuple_to_string(tuples_l[y]))] += 1
            # array at index y. gets from tuple sets, which is converted from binary to an integer as an index and ++

    for x in range(4):
        print(class_h_arrays[x])
    print("")
    for x in range(4):
        print(class_l_arrays[x])


def testing():
    """CPU must determine if the given image is an H or L depending on previous training data"""


def main():
    # creates r_h and r_l, the data sets generated previously
    for x in range(len(DataSet.dataSetH())):
        r_h.append((DataSet.dataSetH()[x][0]))
        r_l.append((DataSet.dataSetL()[x][0]))



    training()
    # print(binary_conversion(convert_tuple_to_string([0, 1, 1])))


main()