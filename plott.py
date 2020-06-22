import matplotlib.pyplot as plt


def create_data_array(list_of_read, tipo, algoritmo, object):
    final_list = []
    for k in list_of_read:
        if object:
            nom_file = "Obj_In-" + str(k) + ".txt"
            file = open("./Test/ObjRes/" + str(algoritmo) + "/" + str(tipo) + "/" + nom_file, "r")
        else:
            nom_file = "In=" + str(k) + ".txt"
            file = open("./Test/"+str(algoritmo)+"/"+str(tipo)+"/"+nom_file, "r")
        final_list.append(float(file.readline(7)))
        file.close()
    return final_list


def draw_graphic(list_input, tipo_input, algoritmo, name, object=False):
    list_x = list_input
    list_y = create_data_array(list_x, tipo_input, algoritmo, object)

    if name == "":

        name = str(algoritmo)
        if tipo_input == "Casuale":
            color = "b"
            mark = "^"
            mk_face_color = "m"
            label = "Input " + str(tipo_input)
        elif tipo_input == "Invertito":
            color = "r"
            mark = "d"
            mk_face_color = "c"
            label = "Input " + str(tipo_input)
        elif tipo_input == "Ordinato":
            color = "g"
            mark = "o"
            mk_face_color = "y"
            label = "Input " + str(tipo_input)
        else:
            color = "w"
            mark = "o"
            mk_face_color = "y"
            label = "Input " + str(tipo_input)
    else:

        if algoritmo == "MergeSort":
            color = "r"
            mark = "d"
            mk_face_color = "c"
        elif algoritmo == "InsertionSort":
            color = "b"
            mark = "o"
            mk_face_color = "m"
        elif algoritmo == "QuickSort":
            color = "g"
            mark = "*"
            mk_face_color = "r"
        elif algoritmo == "RadixSort":
            color = "c"
            mark = "."
            mk_face_color = "r"
        label = str(algoritmo)
    if object:
        plt.xlabel("Memoria occupata (KB)")
        plt.ylabel("Input (num elementi)", labelpad=-5)
        for i in range(0, len(list_y)):
            list_y[i] /= 1024
        plt.plot(list_y, list_x, label=label, color=color, marker=mark, markerfacecolor=mk_face_color)
    else:
        plt.xlabel("Input (num elementi)")
        plt.ylabel("Time (s)")
        plt.plot(list_x, list_y, label=label, color=color, marker=mark, markerfacecolor=mk_face_color)
    plt.legend()
    plt.title(name)


def print_plot():
    plt.show()
