frutas = ["Mango","Pera","Arroz"]
print("lista de futas", frutas)
eliminar = input("¿Que fruta quieres eliminar")

if eliminar in frutas:
    frutas.remove(eliminar)
    print("fruta eliminada")
else:
    print("La fruta no esta en la lista")
print("Lista actualizada", frutas)