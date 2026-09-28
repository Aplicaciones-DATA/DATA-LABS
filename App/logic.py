#Repaso de lógica de programación - Algoritmos de ordenamiento:
#SELECTION SORT

def selection_sort(my_list, sort_criteria):
    #Recorremos la lista en busca del menor 
    fin = len(my_list)
    for i in range(fin - 1):
        #Suponemos que el pirmer elemento es el menor
        min_index = i
        for j in range(i + 1, fin):
            #Extraermos los elementos a comparar
            elemento_actual = get_element(my_list, j)
            elemento_minimo = get_element(my_list, min_index)
            #Comparamos los elemntos con sort_criteria
            if sort_criteria(elemento_actual, elemento_minimo):
                min_index = j
        #Si el minimo no es el que estaba en la posicion i, se intercambian
        if min_index != i:
            exchange_elements(my_list, i, min_index)
            
    return my_list
   