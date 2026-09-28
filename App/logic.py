#Repaso de lógica de programación - Algoritmos de ordenamiento:
#SELECTION SORT

def sort_criteria(element_1, element_2):
    #Verificamos si ambos elementos son enteros
    if isinstance(element_1, int) and isinstance(element_2, int):
        #Extraemos el valor de los elementos, lo convertimos a entero y lo comparamos
        return int(element_1) < int(element_2)
    
    return False

def exchange_elements(my_list, pos_1, pos_2):
    #Evaluamos los valores extremos para evitar errores de indexacion
    if pos_1 < 0 or pos_2 < 0 or pos_1 >= len(my_list) or pos_2 >= len(my_list):
        return f"Error: Posiciones fuera de rango. La lista tiene {len(my_list)} elementos."
    
    #Si las posiciones son iguales, no se realiza el intercambio
    if pos_1 == pos_2:
        return f"Error: Las posiciones son iguales."
    
    #Intercambiamos los elementos en las posiciones especificadas
    my_list[pos_1], my_list[pos_2] = my_list[pos_2], my_list[pos_1]
    
    return my_list



def selection_sort(my_list, sort_criteria):
    #Recorremos la lista en busca del menor 
    fin = len(my_list)
    for i in range(fin - 1):
        #Suponemos que el pirmer elemento es el menor
        min_index = i
        for j in range(i + 1, fin):
            #Extraermos los elementos a comparar
            elemento_actual = my_list[j]
            elemento_minimo = my_list[min_index]
            #Comparamos los elemntos con sort_criteria
            if sort_criteria(elemento_actual, elemento_minimo):
                min_index = j
        #Si el minimo no es el que estaba en la posicion i, se intercambian
        if min_index != i:
            exchange_elements(my_list, i, min_index)
            
    print(my_list)
   

nums = [64, 34, 25, 12, 22, 11, 90]
selection_sort(nums, sort_criteria)