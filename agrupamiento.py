import random

#ESTE CODIGO ESTA IMCOMPLETO YA QUE NO TERMINE EL EJERCICIO

def generar_puntos(cantidad_de_puntos):
    plano  = []

    for _ in range(cantidad_de_puntos):
        num  = random.randint(0,10)
        num2 = random.randint(0,10)
        nums = (num, num2)
        plano.append(nums)
    
    return plano

def union(datos):
    contador = 0
    distancias = []
    for dato in datos:
        datoss = datos[contador + 1]
        print(f'La distancia a medir es de {dato} hasta {datoss}')
        distancia = ((datoss[0] - dato[0])**2+(datoss[1] - dato[1])**2)**0.5
        distancias.append(distancia)
        contador += 1
        cluster = creacion_de_cluster(distancias, dato, datoss)
        if contador > len(datos) - 2:
            break

    return distancias

def creacion_de_cluster(mapa, dato1, dato2):
    cluster = []
    cluster.append(dato1, dato2)
    yield cluster

if __name__ == "__main__":
    cantidad_de_puntos = int(input('Cuantos quieres que haya en el plano? '))
    datos = generar_puntos(cantidad_de_puntos)
    no_se = union(datos)

    print(datos)
    print(no_se)