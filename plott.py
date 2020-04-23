import matplotlib.pyplot as plt


def create_data_array(list_of_read, tipo, algoritmo):
    final_list = []
    for k in list_of_read:
        nom_file = "In="+str(k)+".txt"
        file = open("./Test/"+str(tipo)+"/"+str(algoritmo)+"/"+nom_file, "r")
        final_list.append(file.readline(5))
        file.close()
    return final_list


def draw_graphic(list_input, tipo_input, algoritmo):
    list_x = list_input
    list_y = create_data_array(list_x, tipo_input, algoritmo)
    plt.xlabel("Input")
    plt.ylabel("Time (s)")
    plt.plot(list_x, list_y)
    plt.show()
