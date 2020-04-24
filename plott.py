import matplotlib.pyplot as plt


def create_data_array(list_of_read, tipo, algoritmo):
    final_list = []
    for k in list_of_read:
        nom_file = "In="+str(k)+".txt"
        file = open("./Test/"+str(tipo)+"/"+str(algoritmo)+"/"+nom_file, "r")
        final_list.append(float(file.readline(7)))
        file.close()
    return final_list


def draw_graphic(list_input, tipo_input, algoritmo, name):
    list_x = list_input
    list_y = create_data_array(list_x, tipo_input, algoritmo)
    plt.xlabel("Input (num elementi)")
    plt.ylabel("Time (s)")
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
            label = str(algoritmo)
        elif algoritmo == "InsertionSort":
            color = "b"
            mark = "o"
            mk_face_color = "m"
            label = str(algoritmo)

    plt.plot(list_x, list_y, label=label, color=color, marker=mark, markerfacecolor=mk_face_color)
    plt.legend()
    plt.title(name)


def print_plot():
    plt.show()
