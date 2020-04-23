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
    label = "Input " + str(tipo_input)
    if tipo_input == "Casuale":
        color = "b"
        mark = "^"
        mk_face_color = "m"
    elif tipo_input == "Invertito":
        color = "r"
        mark = "d"
        mk_face_color = "c"
    elif tipo_input == "Ordinato":
        color = "g"
        mark = "o"
        mk_face_color = "y"
    else:
        color = "w"
        mark = "o"
        mk_face_color = "y"
    plt.plot(list_x, list_y, label=label, color=color, marker=mark, markerfacecolor=mk_face_color)
    plt.legend()
    if name == "":
        name = str(algoritmo)
    plt.title(name)


def print_plot():
    plt.show()
