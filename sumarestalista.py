#Crear una funcion recursiva que me de la resta de la 
# suma de los pares menos los impares de una lista


def sumaresta(arr, x):
    if x == 0:
        if arr[0] % 2 == 0:
            return arr[0]
        else:
            return -arr[0]
    else:
        if arr[x] % 2 == 0:
            return arr[x] + sumaresta(arr, x - 1)
        else:
            return -arr[x] + sumaresta(arr, x - 1)

# Prueba
lista = [2, 3, 8, 1]
z = sumaresta(lista, len(lista) - 1)
print("La resta de la suma de pares menos los impares es: ",z)


#OTRO EJEMPLO
def sumRes(lista):
    if len(lista) == 0:
        return 0
    else:
        return sumaresta(lista, len(lista) - 1)

def sumaresta(lista, x) -> int:
    if x == 0:
        #print(f"{x}")
        z = lista[x] if lista[x] % 2 == 0 else - lista[x]
        #print(f"{z} {x}")
        return z
    else:
        #print(f"{x}")
        z = sumaresta(lista, x - 1) + (lista[x] if lista[x] % 2 == 0 else - lista[x])
        #print(f"{z} {x}")
        return z

       

lista = [2,3,8,1]
resultado = sumRes(lista) #10-4=6
print(resultado)