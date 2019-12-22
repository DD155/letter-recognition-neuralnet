import DataSet
import random
import math

tuple_size = 3
num_sets = math.floor(12 / tuple_size)  # amount of sets to be created depending on tuple size
r_h = []
r_l = []


def generate_index_set(index):
    """returns index_arr, array with random indices. uses tuple_size to get num_sets random indices"""
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
    """returns sets, an array that contains all values from data set that correspond to numbers in index set"""
    indices = generate_index_set(index)
    sets = []
    for x in range(len(indices)):
        values = []
        for y in range(tuple_size):
            val = r_h[index][0][indices[x][y]-1]  # value of data set at index [x][y]. -1 is used b/c idx set is 1 to 12
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
    initial_arr = [0, 0, 0, 0, 0, 0, 0, 0]  # array ready for incrementation
    class_h_arrays = [initial_arr, initial_arr, initial_arr, initial_arr]  # 4 arrays in each class
    class_l_arrays = [initial_arr, initial_arr, initial_arr, initial_arr]


def main():
    # creates r_h and r_l, the data sets generated previously
    for x in range(len(DataSet.dataSetH())):
        r_h.append((DataSet.dataSetH()[x][0]))
        r_l.append((DataSet.dataSetL()[x][0]))

    print(binary_conversion(convert_tuple_to_string([1, 1, 1])))


main()