import statistics


def general_dictionary():
    global general_list
    general_list = {}
    with open('iris.data') as data:    # moved file to the project directory
        sample = 1
        for line in data:
            line = line[:len(line) - 1]
            if line == "":        # added: skip empty line
                continue
            general_list[sample] = line.split(",")
            sample += 1
        # print(general_list)
    return general_list


def flowers_quantity(sample):
    global sample_quantity
    sample_quantity = {}
    for element in sample:
        flower_name = sample[element][4]
        if flower_name not in sample_quantity.keys():
            sample_quantity[flower_name] = 1
        else:
            sample_quantity[flower_name] += 1
    # print(sample_quantity)
    kind_of_flowers()
    return sample_quantity


def kind_of_flowers():         # defining dictionary for each kind of flower
    for element in sample_quantity:
        flower_kind = {}
        count = 1
        for key in general_list:
            if element in general_list[key]:
                flower_kind[count] = general_list[key]
                count += 1
        # print(flower_kind)
        count_average(flower_kind)


def count_average(flower):             # used mean built-in function
    avg = statistics.mean((map(float, (flower[element][0] for element in flower))))
    print(flower[1][4], round(avg, 2))


if __name__ == '__main__':
    flowers_quantity(general_dictionary())
