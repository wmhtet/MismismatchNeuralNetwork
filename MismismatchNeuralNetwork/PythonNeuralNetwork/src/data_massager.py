
ALL_DIFFERENT_ATTRIBUTE = 0

def read_file(solution_type):
    string_tuple_list = []
    f = open('../data/MMM_NN_TRAING_DATA', 'r')
    for line in f:
        inout = line.rstrip().split(":")
        string_tuple_list.append((inout[0], inout[1]))
    f.close()

    path = {
        ALL_DIFFERENT_ATTRIBUTE: "../data/ALL_DIFFERENT_ATTRIBUTE",
        'b': "",
        'c':""
    }[solution_type]
    sf = open(path, 'r')
    solutions = set()
    for line in sf:
        str_array = line.rstrip().split(" ")
        sol = frozenset(str_array)
        # print(sol)
        solutions.add(sol)
    return string_tuple_list, solutions


"""
3RBE 2OGS 2DGL 1DRS 1OGS 3DGS 1OBL 3ORE 1RBS 3OBE 1RRE 1RGL:2 7 8|4 8 3|8 11 10|6 7 1|
w = open('../data/MASSAGED_DATA', 'w')
for l in training_data:
    formatted_string = "{0} _:_ {1}\n".format(' '.join(map(str, l[0].flatten())), ' '.join(map(str, l[1].flatten())))
    w.write(formatted_string)
w.close()  """


# Create a solution set that is sorted for comparison
def multiple_sorted_int_array(str_data):
    sln_set = set()
    if len(str_data) == 0:
        return sln_set
    sln_array = str_data[:-1].split("|")
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

def massage_data(solution_type):
    string_tuple_list, solutions = read_file(solution_type)
    massaged_data = []
    # print(solutions)
    for t in string_tuple_list:
        solutionSets = multiple_sorted_int_array(t[1])
        solutions_checked = check_solution(t[0], solutions, solutionSets)
        if solutions_checked != "":
            massaged_data.append((t[0], solutions_checked))

    path = {
        ALL_DIFFERENT_ATTRIBUTE: "../data/ALL_DIFFERENT_ATTRIBUTE_TRAINING_DATA",
        'b': "",
        'c':""
    }[solution_type]
    w = open(path, 'w')
    for l in massaged_data:
        formatted_string = "{0}:{1}\n".format(l[0],l[1])
        w.write(formatted_string)
    w.close()

    print(string_tuple_list[0:5])
    print("---------")
    print(len(string_tuple_list))
    print(massaged_data[0:5])
    print("---------")
    print(len(massaged_data))

def massage_data_all_different():
    massage_data(ALL_DIFFERENT_ATTRIBUTE)


def all_different_attribute(cards_array, solutionSets):
    pass


def check_solution(str_data, solutions, solutionSets):
    if len(solutionSets) == 0 :
        return ""
    cards_array = str_data.split(" ")
    count = len(cards_array)
    sol_str_array = []
    sln_set = set()
    for first in range(count):
        for second in range(count):
            for third in range(count):
                if first != second and second != third and first != third :
                    first_card = cards_array[first]
                    second_card = cards_array[second]
                    third_card = cards_array[third]

                    sol = frozenset([first_card, second_card, third_card])
                    if sol in solutions:
                        sol_str = "{0} {1} {2}".format(first, second, third)
                        sln_int_array = string_to_sorted_int_array(sol_str)

                        if (sln_int_array[0], sln_int_array[1], sln_int_array[2]) not in sln_set:
                            sln_set.add((sln_int_array[0], sln_int_array[1], sln_int_array[2]))
                            sol_str_array.append(sol_str)

                        if (sln_int_array[0], sln_int_array[1], sln_int_array[2]) not in solutionSets:
                            tmp = "{0} is not in {1}".format(sol_str, solutionSets)
                            print(tmp)

    if len(sol_str_array) == 0:
        return ""

    return "|".join(sol_str_array)
