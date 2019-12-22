import random

random.seed(50)  # set constant seed so data set will be same every time program is run


def visual_representation(arr):
    for x in range(len(arr)):
        if arr[x] == 1:
            print("X", end=" ")
        else:
            print(" ", end=" ")
        if ((x + 1) % 3) == 0:
            print("")
    print("------")


def gen_arrays_H():
    # constraints for H
    # indices 1, 10 must always be 0.
    # indices 3, 6, 5, 8, 4, 7 must have at least one 1
    for x in range(30):
        # creates list of indices with either 0 or 1
        append_data = [[random.randint(0, 1), 0, random.randint(0, 1), random.randint(0, 1), random.randint(0, 1),
                       random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1),
                       random.randint(0, 1), 0, random.randint(0, 1)]]
        # makes sure that indices 3, 6, 5, 8, 4, 7 have at least one 1
        if append_data[0][3] == 0 and append_data[0][4] == 0: append_data[0][(random.randint(3,4))] = 1
        if append_data[0][5] == 0 and append_data[0][6] == 0: append_data[0][(random.randint(5, 6))] = 1
        if append_data[0][7] == 0 and append_data[0][8] == 0: append_data[0][(random.randint(7, 8))] = 1
        visual_representation(append_data[0])


def gen_arrays_L():
    l1 = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1]
    listL = []
    for x in range(30):
        listL.append([1, 0, 0, 1, 0, 0, random.randint(0, 1), random.randint(0, 1), random.randint(0, 1),
                      random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)])

    return listL


def dataSetL():
    # acceptable generated arrays for L, chose 15 to duplicate to 300
    l1 = [[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1], "L"]
    l2 = [[1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0], "L"]
    l3 = [[1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], "L"]
    l4 = [[1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0], "L"]
    l5 = [[0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1], "L"]
    l6 = [[0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1], "L"]
    l7 = [[1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1], "L"]
    l8 = [[1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1], "L"]
    l9 = [[1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1], "L"]
    l10 = [[1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0], "L"]

    data_l = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]
    data_set_l = []
    for x in range(300):
        new_data = [data_l[random.randint(0, 9)], "L"]
        data_set_l.append(new_data)

    return data_set_l


def dataSetH():
    # acceptable generated arrays for H, chose 15 to duplicate to 300
    h1 = [[1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1], "H"]
    h2 = [[1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1], "H"]
    h3 = [[1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1], "H"]
    h4 = [[1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1], "H"]
    h5 = [[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1], "H"]
    h6 = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], "H"]
    h7 = [[1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1], "H"]
    h8 = [[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1], "H"]
    h9 = [[0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1], "H"]
    h10 = [[1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1], "H"]
    h11 = [[1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0], "H"]
    h12 = [[1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1], "H"]
    h13 = [[0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1], "H"]
    h14 = [[1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1], "H"]
    h15 = [[0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1], "H"]

    data_h = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15]  # new array to store accepted values
    data_set_h = []  # actual data set for H
    for x in range(300):  # generate random amount of each accepted array to put into data set
        new_data = [data_h[random.randint(0, 14)], "H"]
        data_set_h.append(new_data)

    return data_set_h
