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
            
    
    
#HASHING - TABLAS DE HASH Y FUNCIONES HASH

#Ejercicio 1: Simu parcial 
def find_slot_with_increment(my_map, key, hash_value, delta):
    #Verificamos que el arreglo del map no esté vacio 
    if not my_map:
        return "Error: arreglo vacío"
    
    #Recorremos el arreglo del map para encontrar el slot vacio 
    
    encontrado = False
    pos_actual = hash_value
    
    for intento in range(len(my_map["table"])):
        entry = my_map["table"][pos_actual]
        
        #Evaluamos si es igual a la key que buscamos 
        if entry["key"] == key:
            encontrado = True 
            return (encontrado, pos_actual)
        
        #Evaluamos si el slot está vacio
        elif entry["key"] is None:
            encontrado = False
            return (encontrado, pos_actual)
        
        #Evaluamos si el slot tiene una key eliminada
        elif entry["key"] == "_EMPTY_":
            encontrado = False
            pos_actual = (pos_actual + delta) % len(my_map["table"])
                    
        #Evaluamos si el slot está ocupado por una key diferente            
        elif entry["key"] != key:
            #Si el slot está ocupado, incrementamos la posicion con delta
            pos_actual = (pos_actual + delta) % len(my_map["table"])
            
            
    return (encontrado, None)

            
pass






#PREPARACIÓN PARA EL PARCIAL 1 DE DATA:
#- Trabajaremos con el contenido de uno de los laboratorios anteriores de "DATA"
#- Haremos el EDA y el ETL de los datos para poder analizarlos y obtener información de ellos 

#step 1: Importamos las librerias
import pandas as pd 
import matplotlib.pyplot as plt


#step 2: Cargamos el dataset y creamos la copia de trabajo

df = pd.read_csv("Data/bicicletas_compartidas_bogota.csv")
df_limpio = df.copy()

#step 3: Hacemos la revision inicial de los datos 
display(df.shape())
display(df.columns())
display(df.head())
display(df.info())

#step 4: Revisamos la calidad d elos datos 
display(df.isna().sum())
display(df.duplicated().sum())

#step 5: Hacemos lo que piden 

#1: calculamos la correlaciuon de pearson con la distancia y el tiempo de viaje
correlacion_dt = df_limpio["distancia_km"].corr(df_limpio["tiempo_viaje"])

print(correlacion_dt)


#2: Calcular el IQR de la distancia y el tiempo del viaje y los limites
q1 = df_limpio["distancia_km"].quantile(0.25)
q3 = df_limpio["distancia_km"].quantile(0.75)
iqr = q3 - q1

#limites
limite_infe = q1 - 1.5 * iqr
limite_supe = q3 + 1.5 * iqr

pass


#CLASE SOBRE DATOS ABIERTOS Y APIs: 

#Importar batos en CSV desde una URL:
import pandas as pd
import requests

url = "https://www.datos.gov.co/api/v3/views/mvrj-vu7n/query.json"
response = requests.post(url)













    












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   

