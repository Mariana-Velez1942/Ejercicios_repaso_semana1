#Pide 5 números y crea una lista solo con los pares.
 # creo dos listas vacias 

numeros =[] # se generan las dos variables 
numerospares = []

for i in range(5): # se utliza un ciclo for en un range para una secuencia de numeros enteros: Se genera una iteracion de de o a 5
    numeros = int(input(f"ingresa el numero {i+1}:"))
    numerospares.append(numeros) #utilizamos el append para agregar un ultimo elemento en la lista
    if numeros %2 ==0: 
        numerospares.append(numeros)
        print("numeros ingresados",numeros)
        print("numeros pares",numerospares)