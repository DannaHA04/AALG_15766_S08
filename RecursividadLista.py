#Haga una funcion que obtenga la suma de los elementos de una lista

#funcion recursiva
def suma(arr, x) -> int:
    if x == 0:
        return arr[0]
    else:
        return arr[x] + suma(arr, x - 1)

lista = [5,8,7,2]

z = suma (lista, len(lista) - 1)
print(z)

#wrapper
def sumaLista(arr):
    if len(arr) > 0:
        suma(arr, len(arr) - 1)
    else:
        return 0

lista1 = []
g = sumaLista(lista1)
print(g)