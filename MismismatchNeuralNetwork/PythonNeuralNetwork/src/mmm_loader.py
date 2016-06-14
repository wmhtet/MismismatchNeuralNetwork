

# Third-party libraries
import numpy as np
# import network


def load_data():
    f = open('../data/MMM_NN_TRAING_DATA', 'r')
    string_tuple_list = []
    print("4")
    for line in f:
        inout = line.rstrip().split(":")
        string_tuple_list.append((inout[0], inout[1]))

    f.close()
    training_data = []
    for t in string_tuple_list[20002:300002]:
        training_data.append((string_to_massaged_float_array(t[0]), string_to_out_put_index(t[1])))

    validation_data = []
    for t in string_tuple_list[10001:20001]:
        validation_data.append((string_to_massaged_float_array(t[0]),  string_to_sorted_int_array(t[1])))

    test_data = []
    for t in string_tuple_list[0:10000]:
        test_data.append((string_to_massaged_float_array(t[0]),  string_to_sorted_int_array(t[1])))

    formatted = "{0} : \n {1} :   ".format(training_data[0][0],training_data[0][1], )
    formatted2 = "{0} : {1} : {2} ".format(np.shape(training_data), training_data[0][0].size, len(training_data[0][1]))
    # print (data_list[0])
    print(formatted)
    print(formatted2)
    # training_data, validation_data, test_data = data_list, data_list[10001:20001], data_list[0:10000]
    # net = network.Network([input_length, 49, output_length])
    # net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
    return training_data, validation_data, test_data


def string_to_out_put_index(str_data):
    str_array = str_data.split(" ")
    u_int_array = np.zeros(shape=(12, 1))
    for n in str_array:
        u_int_array[int(n)] = 1
    return u_int_array


def string_to_sorted_int_array(str_data):
    str_array = str_data.split(" ")
    int_array = []
    for n in str_array:
        int_array.append(int(n))
    return sorted(int_array)


def string_to_sorted_int_vector(str_data):
    str_array = str_data.split(" ")
    int_array = np.zeros(shape=(3, 1))
    i = 0
    for n in str_array:
        int_array[i] = (int(n))
        i += 1
    return sorted(int_array)

# NUMBERS = ["1","2","3"]
# SHAPES = ["R", "O", "D"]
# COLORS = ["R", "G", "B"]
# FILLINGS = ["E", "S", "L"]


getVal = {
    "1": [1.0, 0.0, 0.0],
    "2": [0.0, 1.0, 0.0],
    "3": [0.0, 0.0, 1.0],
    "R": [1.0, 0.0, 0.0],
    "O": [0.0, 1.0, 0.0],
    "D": [0.0, 0.0, 1.0],
    "G": [0.0, 1.0, 0.0],
    "B": [0.0, 0.0, 1.0],
    "E": [1.0, 0.0, 0.0],
    "S": [0.0, 1.0, 0.0],
    "L": [0.0, 0.0, 1.0],
}


def string_to_massaged_float_array(str_data):
    str_data = str_data.replace(" ", "")
    u_int_array = []  # np.zeros(shape=(144, 1))
    for ch in str_data:
        u_int_array.append(getVal[ch])

    np_array_data = np.array(u_int_array, dtype=np.float32).reshape((144, 1))
    # print(type(np_array_data))
    # return np_array_data.reshape(len(np_array_data), 1)
    return np_array_data


def string_to_unicode_float_array(str_data):
    u_int_array = np.zeros(shape=(48, 1))
    i = 0
    for ch in map(ord, str_data):
        val = np.float32(ch)  # / 100000.0
        # val_in_array = np.array([val], dtype=np.float32)
        if val != 32.0:
            u_int_array[i] = val
            i += 1
    np_array_data = np.array(u_int_array, dtype=np.float32)
    # print(type(np_array_data))
    # return np_array_data.reshape(len(np_array_data), 1)
    return np_array_data


def pad_output(data_need_to_pad):
    size = 7 - len(data_need_to_pad)
    if size == 0:
        return data_need_to_pad
    u_int_array = []
    for i in range(size):
        val = np.float32(0)
        val_in_array = np.array([val], dtype=np.float32)
        u_int_array.append(val_in_array)

    np_array_data = np.array(u_int_array, dtype=np.float32)
    new_np_array_data = np.append(data_need_to_pad, np_array_data)
    return new_np_array_data.reshape(len(new_np_array_data), 1)
