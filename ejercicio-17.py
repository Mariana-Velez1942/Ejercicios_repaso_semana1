# se usa count para contar los elementos de una lista

lista = ["mariana","fernando","luis","pedro","juan"]

nombre_buscado = input("ingresa un nombre para poder contar : ")

cantidad = lista.count(nombre_buscado)
print(f"El nombre {nombre_buscado} aparece  {cantidad} de veces ")