file_name = "C:\\Users\\Lena_Laptop\\Documents\\Python\\FILES\\iris.data"


def general_dictionary(filename):
    global general_list
    general_list = {}
    with open(filename) as data:
        sample = 1
        for line in data:
            line = line[:len(line) - 1]
            general_list[sample] = line.split(",")
            sample += 1
        del general_list[len(general_list)]
        # print (general_list)
    return general_list


def kind_of_flowers():
    general_dictionary(file_name)
    iris_setosa_list()
    iris_versicolor_list()
    iris_virginica_list()


def iris_setosa_list():
    iris_setosa = {}
    count = 1
    for key in general_list:
        if 'Iris-setosa' in general_list[key]:
            iris_setosa[count] = general_list[key]
            count += 1
    # print(iris_setosa)
    count_average(iris_setosa)
    return iris_setosa


def iris_versicolor_list():
    iris_versicolor = {}
    count = 1
    for key in general_list:
        if 'Iris-versicolor' in general_list[key]:
            iris_versicolor[count] = general_list[key]
            count += 1
    # print(iris_versicolor)
    count_average(iris_versicolor)
    return iris_versicolor


def iris_virginica_list():
    iris_virginica = {}
    count = 1
    for key in general_list:
        if 'Iris-virginica' in general_list[key]:
            iris_virginica[count] = general_list[key]
            count += 1
    # print(iris_virginica)
    count_average(iris_virginica)
    return iris_virginica


def count_average(flower):
    total = 0
    for element in flower:
        total += float(flower[element][0])
    # print(round(sum, 2))
    average_growth = total/len(flower)
    # print(round(average_growth, 2))
    print(flower[1][4], round(average_growth, 2))


if __name__ == '__main__':
    kind_of_flowers()
