# se utiliza .insert 
# #Agregar un número en una posición específica.

lista = [2,4,6,8,10] # se realiza la lista

agregar_numero = int(input("Agrega un nuevo numero")) # se genera la variable y el mensaje
posicion = int(input("en que posicion de (0-10): ")) # se genera otra variable e imprimimos en que posicion debe estar nuestro numero

lista.insert(posicion,lista) # se usa insert para agregar el numero en una posicion especifica
print("Lista actualizada", lista) # se imprime la lista actualizada y se invoca la lista para poder mostrar el resultado de la lista
