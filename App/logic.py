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
    
pass


#Ejericio 2:

def sort_criteria(pedido_1, pedido_2):
    #Comparamos el tiempo de los pedidos
    if pedido_1[1] < pedido_2[1]:
        return True
    
    elif pedido_1[1] == pedido_2[1]:
        if pedido_1[0] < pedido_2[0]:
            return True
    return False

def xchange_pedidos(lista, pos1, pos2):
    #Evaluamos los valores extremos:
    if pos1 < 0 or pos1 >= len(lista) or pos2 < 0 or pos2 >= len(lista):
        return "Error: posicion fuera de rango"
    
    #Evaluamos si son iguales 
    if pos1 == pos2:
        return "Error: posiciones iguales"
    
    #Hacemos el switch
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
    
    return lista

def sort_pedidos(pedidos:list, sort_criteria, xchange_pedidos):
    #Verificamos que la lista no esté vacía
    if not pedidos:
        return "Error: Lista vacia"
    
    #Verificamos que todos los elementos de la lista sean tuplas
    for pedido in pedidos:
        if not isinstance(pedido, tuple):
            return "Error: Más de una tipo de dato en la lista"
        
    #Hacemos la comparación del tiempo de los pedidos
    for i in range(len(pedidos) - 1):
        #Suponemos que el menor es el pirmero
        menorp_index = i 
        
        for j in range(i + 1, len(pedidos)):
            #Comparamos 
            menor_p = pedidos[menorp_index]
            actual_p = pedidos[j]
            
            if sort_criteria(actual_p, menor_p):
                menorp_index = j 
                
        #Si el minimo no es el que está en i, se hace el switch 
        if menorp_index != i: 
            xchange_pedidos(pedidos, i, menorp_index)
    return pedidos  
             
    
lista_pedidos = [
    ("P14", 20), ("P03", 12), ("P10", 12), ("P08", 35),
    ("P22", 15), ("P01", 45), ("P17", 8),  ("P05", 25),
    ("P11", 18), ("P09", 30), ("P19", 14), ("P02", 50),
    ("P07", 22), ("P25", 10), ("P04", 40), ("P15", 28),
    ("P21", 17), ("P06", 33), ("P13", 21), ("P20", 9),
    ("P12", 24), ("P24", 19), ("P18", 27), ("P23", 11),
    ("P16", 31)
]

print(sort_pedidos(lista_pedidos, sort_criteria, xchange_pedidos))

pass



#INSERTION SORT - ALGORITMO DE ORDENAMIENTO 

def sort_criteria(prod1, prod2):
    #Comparamos los dicts por preciounidad
    if prod1["preciounidad"] < prod2["preciounidad"]:
        return True
    
    return True
    
def insertion_sort(productos, n, sort_criteria):
    #n == cuantos elementos queremos retornar
    
    #Evaluamos que la lista no esté vacia
    if not productos:
        return "Error: lista vacia"
    
    #Evaluamos si todos los elementosa son dicts
    for producto in productos:
        if not isinstance(producto, dict):
            return "Error: más de un tipo de dato en la lista"
        
    #Hacemos el recorrido y la comparativa
    for i in range(1, len(productos)):
        actual = productos[i]
        j = i - 1
        while j >= 0 and productos[j] > actual:
            #Si el valor del indice de la izquierda (parte ordenada), es mayor que el que estamos revisando, lo movemos a la derecha
            productos[j + 1] = productos[j]
            
            #Restamos 1 a j para seguir iterando de derecha a izquierda
            j -= 1
            
        
        productos[j + 1] = actual 
        
    return productos 
            
    
            
        

    












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   

