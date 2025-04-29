lista = [2,30,50,40,15]

buscado = (input("Ingrese un numero para buscar : "))

if buscado in lista: # si buscado esta en lista
    posicion = lista.index(buscado) # entonces la posicion(Es una nueva variable que permite buscar la posicion)
    #lista.index permite buscar la posicion en la lista
    print(f"El numero {buscado} esta en la posicion {posicion}: ") # se utiliza un f string para que imprima tanto el resultado como la variable
else:
    print(f"el numero {buscado} esta en la lista")