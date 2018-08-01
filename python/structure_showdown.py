import importlib
import time

linked_list = importlib.import_module("LinkedList")
binary_tree = importlib.import_module("BinaryTree")
hash_table = importlib.import_module("HashTable")

print("Comparación de rendimiento entre Lista Enlazada, Árbol de Búsqueda Binaria y Tabla de Hash.")

length = int(input("Ingresa la cantidad de elementos : "))

lista = linked_list.LinkedList()
arbol = binary_tree.BinaryTree()
tabla = hash_table.HashTable(50)

start = time.time()

for i in range(length) :
  lista.insert(i)
  arbol.insert(i)
  tabla.insert(i,str(i))

print(str(length) + " objetos insertados en " + str(time.time() - start) + " segundos.")

start = time.time()

for i in range(length) :
  lista.find(i)
  arbol.find(i)
  tabla.find(str(i))

print(str(length) + " objetos encontrados en " + str(time.time() - start) + " segundos.")

print("Lista Enlazada :")
print("\tTiempo promedio de inserción : " + str(lista.getAvgInsertionTime()) + " segundos.")
print("\tTiempo promedio de búsqueda : " + str(lista.getAvgSearchTime()) + " segundos.")

print("Árbol Binario :")
print("\tTiempo promedio de inserción : " + str(arbol.getAvgInsertionTime()) + " segundos.")
print("\tTiempo promedio de búsqueda : " + str(arbol.getAvgSearchTime()) + " segundos.")

print("Tabla de Hash :")
print("\tTiempo promedio de inserción : " + str(tabla.getAvgInsertionTime()) + " segundos.")
print("\tTiempo promedio de búsqueda : " + str(tabla.getAvgSearchTime()) + " segundos.")