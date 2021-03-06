

# Third-party libraries
import numpy as np
import random
import network
import datetime as dt

# import mmm_loader
# import network
# training_data, validation_data, test_data = mmm_loader.load_data()
# net = network.Network([144,48,12])
# net.SGD(training_data, 30, 10, 3.0, test_data=test_data)


OUTPUT_NODE = 12
OUTPUT_UNROLL_NODE = 36

def read_file():
    print(dt.datetime.now().minute)
    string_tuple_list = []
    f = open('../data/MMM_NN_TRAING_DATA', 'r')   # MMM_NN_TRAING_DATA ALL_DIFFERENT_ATTRIBUTE_TRAINING_DATA
    for line in f:
        # use number less than 70 to limits the solution to 1
        # or use big numbers like 1000 to remove that restriction
        #
        # or use number greater than 61<?> to strip the data with no solution
        if len(line) > 61:
            inout = line.rstrip().split(":")
            string_tuple_list.append((inout[0], inout[1]))
    f.close()
    random.shuffle(string_tuple_list)
    return string_tuple_list


def print_answer_number_count(data_list, param):
    u_int_array = np.zeros(shape=(OUTPUT_NODE, 1))
    # print(u_int_array)
    print(data_list[0][1])
    for data in data_list:
        indx = data[1]
        val =  u_int_array[indx]
        u_int_array[indx] = val + 1
    print(param)
    print(u_int_array.flatten())
    print(u_int_array.flatten().argsort()[::-1])


def print_answer_number_count_list(data_list, param):
    u_int_array = np.zeros(shape=(OUTPUT_NODE, 1))
    # print(u_int_array)
    print(data_list[0][1])
    for data in data_list:
        u_int_array += data[1]

    print(param)
    print(u_int_array.flatten())
    print(u_int_array.flatten().argsort()[::-1])


def print_data(string_tuple_list, training_data, validation_data, test_data, print_flag=None):
    print(string_tuple_list[0])
    formatted = "{0} : {1} :   ".format(test_data[0][0].flatten(), test_data[0][1], )
    formatted2 = "{0} : {1} : {2} ".format(np.shape(test_data), test_data[0][0].size, test_data[0][1])
    # formatted = "{0} : {1} :   ".format(training_data[0][0].flatten(), training_data[0][1], )
    #formatted2 = "{0} : {1} : {2} ".format(np.shape(training_data), training_data[0][0].size, training_data[0][1])
    # print (data_list[0])
    print(formatted)
    print(formatted2)
    network.print_list(string_tuple_list[20059:20064])
    print_flatten_tuple_list(training_data[57:62])

    network.print_list(string_tuple_list[30:35])
    print_flatten_tuple_list_(test_data[30:35])

#    print_answer_number_count_list(training_data, "training_data")
    # print_answer_number_count(test_data, "test_data")
    """
    w = open('../data/MASSAGED_DATA', 'w')
    for l in training_data:
        formatted_string = "{0} _:_ {1}\n".format(' '.join(map(str, l[0].flatten())), ' '.join(map(str, l[1].flatten())))
        w.write(formatted_string)
    w.close()  """


def print_flatten_tuple_list(ls):
    for l in ls:
        print("{0} : {1}".format(l[0].flatten(), l[1].flatten()))


def print_flatten_tuple_list_(ls):
    for l in ls:
        print("{0} : {1}".format(l[0].flatten(), l[1]))

def load_data():
    string_tuple_list = read_file()
    training_data = []
    print_flag = True        # 132805
    for t in string_tuple_list[20002:]:
        sln_array = t[1].split("|")
        for sln in sln_array:
            sln_int_array = string_to_out_put_index(sln, print_flag)
            training_data.append((string_to_massaged_float_array(t[0], print_flag), sln_int_array))
            print_flag = False

    validation_data = []
    for t in string_tuple_list[10001:20001]:
        validation_data.append((string_to_massaged_float_array(t[0]),  multiple_sorted_int_array(t[1])))

    test_data = []
    for t in string_tuple_list[0:10000]:
        test_data.append((string_to_massaged_float_array(t[0]),  multiple_sorted_int_array(t[1])))

    print_data(string_tuple_list, training_data, validation_data, test_data, print_flag)

    random.shuffle(validation_data)
    random.shuffle(training_data)
    random.shuffle(test_data)
    # training_data, validation_data, test_data = data_list, data_list[10001:20001], data_list[0:10000]
    # net = network.Network([input_length, 49, output_length])
    # net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
    return training_data, validation_data, test_data


def load_data_num_sol():
    string_tuple_list = read_file()
    training_data = []
    print_flag = True
    for t in string_tuple_list[20002:]:
        count = string_to_out_put_count_array(t[1])
        training_data.append((string_to_massaged_float_array(t[0], print_flag), count))
        print_flag = False

    validation_data = []
    for t in string_tuple_list[10001:20001]:
        sln_array = t[1][:-1].split("|")
        for sln in sln_array:
            count = string_to_out_put_count(sln)
            validation_data.append((string_to_massaged_float_array(t[0]),  count))

    test_data = []
    for t in string_tuple_list[0:10000]:
        count = 0
        if len(t[1]) != 0:
            sln_array = t[1][:-1].split("|")
            count = len(sln_array)
        test_data.append((string_to_massaged_float_array(t[0]),  count))

    print_data(string_tuple_list, training_data, validation_data, test_data, print_flag)

    random.shuffle(validation_data)
    random.shuffle(training_data)
    random.shuffle(test_data)
    return training_data, validation_data, test_data


def load_data_output_unroll():
    string_tuple_list = read_file()
    training_data = []
    print_flag = True        # 132805
    for t in string_tuple_list[20002:]:
        sln_array = t[1].split("|")
        for sln in sln_array:
            sln_int_array = string_to_out_put_index_unroll(sln, print_flag)
            training_data.append((string_to_massaged_float_array(t[0], print_flag), sln_int_array))
            print_flag = False

    validation_data = []
    for t in string_tuple_list[10001:20001]:
        validation_data.append((string_to_massaged_float_array(t[0]),  multiple_sorted_int_array(t[1])))

    test_data = []
    for t in string_tuple_list[0:10000]:
        test_data.append((string_to_massaged_float_array(t[0]),  multiple_sorted_int_array(t[1])))

    print_data(string_tuple_list, training_data, validation_data, test_data, print_flag)

    random.shuffle(validation_data)
    random.shuffle(training_data)
    random.shuffle(test_data)
    # training_data, validation_data, test_data = data_list, data_list[10001:20001], data_list[0:10000]
    # net = network.Network([input_length, 49, output_length])
    # net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
    return training_data, validation_data, test_data


def multiple_slns_index(str_data):
    sln_array = str_data[:-1].split("|")
    u_int_array = np.zeros(shape=(120, 1))
    # print("=====")
    for sln in sln_array:
        sln_int_array = string_to_out_put_index(sln)
        indx = get_index_from_binary_value(sln_int_array.flatten())
        indx_range = np.arange(indx, indx+12)
        # print(indx_range)
        # print(sln_int_array.flatten())
        # print(u_int_array.flatten())
        np.put(u_int_array, indx_range, sln_int_array)
        # print(u_int_array.flatten())
    return u_int_array


def get_index_from_binary_value(int_array):
    binary_str = "".join([str(int(x)) for x in int_array])
    int_val = int(binary_str, 2)
    # format = "{0}:{1}:{2}".format(int_val, binary_str, int_val/358)
    # print(format)
    return int_val/358

count_empty = 0

def string_to_out_put_count(str_data):
    if len(str_data) == 0:
        # print('c', end="", flush=True)
        return 0
    str_array = str_data.split(" ")
    return len(str_array)


def string_to_out_put_count_array(str_data, print_flag=None):
    u_int_array = np.zeros(shape=(OUTPUT_NODE, 1))

    if len(str_data) == 0:
        # print('.', end="", flush=True)
        u_int_array[0] = 1
        return u_int_array

    sln_array = str_data[:-1].split("|")
    u_int_array[len(sln_array)] = 1
    if print_flag:
        print("{0}:{1}".format(str_data, u_int_array.flatten()))
    return u_int_array


# answer string to  0,1 array of length 12 with index
# which is present in the answer having value 1s while the rest having 0s
def string_to_out_put_index(str_data, print_flag=None):
    u_int_array = np.full((OUTPUT_NODE, 1), -1)
    # print(str_data)
    if len(str_data) == 0:
        return u_int_array
    str_array = str_data.split(" ")
    for n in str_array:
        u_int_array[int(n)] = 1
    if(print_flag):
        print("{0}:{1}".format(str_data, u_int_array.flatten()))
    return u_int_array

def str_to_int(str):
    return int(str)


# answer string to  0,1 array of length 36(12x3) with index
# which is present in the answer having value 1 while the rest having 0s
# in each 12 nodes section for 3 answers of 36 nodes output
def string_to_out_put_index_unroll(str_data, print_flag=None):
    u_int_array = np.full((OUTPUT_UNROLL_NODE, 1), -1)
    # print(str_data)
    if len(str_data) == 0:
        return u_int_array
    str_array = sorted(map(str_to_int, list(str_data.split(" "))))
    pos = 0
    for n in str_array:
        u_int_array[n + (pos * OUTPUT_NODE)] = 1
        pos += 1
    if(print_flag):
        print("string_to_out_put_index_unroll")
        print("{0}:{1}".format(str_data, u_int_array.flatten()))
    return u_int_array


# Create a solution set that is sorted for comparison
def multiple_sorted_int_array(str_data):
    sln_array = str_data.split("|")
    sln_set = set()
    for sln in sln_array:
        if len(sln) != 0:
            sln_int_array = string_to_sorted_int_array(sln)
            sln_set.add((sln_int_array[0], sln_int_array[1], sln_int_array[2]))
    return sln_set


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

    # R for Red has the same value as R for Round
    "G": [0.0, 1.0, 0.0],
    "B": [0.0, 0.0, 1.0],

    "E": [1.0, 0.0, 0.0],
    "S": [0.0, 1.0, 0.0],
    "L": [0.0, 0.0, 1.0],
}


def string_to_massaged_float_array(str_data, print_flag=None):
    str_data = str_data.replace(" ", "")
    u_int_array = []  # np.zeros(shape=(144, 1))
    for ch in str_data:
        u_int_array.append(getVal[ch])

    np_array_data = np.array(u_int_array, dtype=np.float32).reshape((144, 1))

    if print_flag:
        print("----string_to_massaged_float_array-----")
        print(str_data)
        print(u_int_array)
        print(np_array_data.flatten())
        print("----string_to_massaged_float_array-----")
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
