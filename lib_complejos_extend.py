import lib_complejos as lb
import math
 


def sum_vector(a,b):
    resultado = [(0,0)] * len(a)
    for x in range(len(a)):
        resultado[x] = lb.suma_complejos(a[x],b[x])

    return resultado


def esc_vector(a,b):
    resultado = [(0,0)] * len(a)
    for x in range(len(a)):
        resultado[x] = lb.multiplicacion_complejos(b,a[x])
    return resultado

def resta_vector(a,b):
    resultado = [(0,0)] * len(a)    
    for x in range(len(a)):
        resultado[x] = lb.resta_complejos(a[x],b[x])

    return resultado

def inverso_aditivo_vector(a):
    resultado = [(0,0)] * len(a)
    
    for x in range(len(a)):
        resultado[x] = lb.multiplicacion_complejos(a[x],(-1,0))

    return resultado

def suma_Matriz(a,b):
    
    if (len(a)!= len(b)) or (len(a[0])!= len(b[0])):
        messagebox.showerror("ERROR!","Los matrices pueden ser operadas, no son de igual dimension")
    else:
        resultado  = [[None for i in range(len(a[0]))] for j in range(len(a))]

        for i in range(len(a)):
            for j in range(len(a[0])):
                resultado[i][j] = lb.suma_complejos(a[i][j],b[i][j])

        return resultado

def inversoAditivo_Matriz(a):
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = lb.multiplicacion_complejos(a[i][j],[-1,0])

    return a

def productoEscalar_Matriz(a,b):
 
    resultado = [[None for i in range(len(a[0]))] for j in range(len(a))]

    for i in range(len(a)):
        for j in range(len(a[0])):
            resultado[i][j] = lb.multiplicacion_complejos(a[i][j],b)

    return resultado

def transpuesta_Matriz_Vector(a):
   
    respuesta = [[None for i in range(len(a))] for j in range(len(a[0]))]

    for i in range(len(a)):
        for j in range(len(a[0])):
            respuesta[j][i] = a[i][j]

    return respuesta

def conjugado_Matriz_Vector(a):

    resultado = [[None for j in range(len(a[0]))] for i in range(len(a))]

    if len(a[0]) > 1:
        for i in range(len(a)):
            for j in range(len(a[0])):
                resultado [i][j] = lb.conjugado_complejos(a[i][j])

    else:
        for i in range(len(a)):
            resultado [i][0] = lb.conjugado_complejos(a[i][0])

    return resultado


def adjunta_Matriz_Vector(a):
    p = a[:]
    d = conjugado_Matriz_Vector(p)
    transpuesta = transpuesta_Matriz_Vector(d)

    return transpuesta
def producto_Matriz(a,b):

    if len(a[0]) != len(b):
        messagebox.showerror("ERROR!","Los matrices pueden ser operadas, no son compatibles")
    else:
        respuesta = [[[0,0] for i in range(len(b[0]))] for j in range(len(a))]

        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    respuesta[i][j] = lb.suma_complejos(respuesta[i][j],lb.multiplicacion_complejos(a[i][k],b[k][j]))

        return respuesta


def accion_MatrizSobreVector(a,b):
    return producto_Matriz(a,b)

def productoInterno_Vector(a,b):

    s = adjunta_Matriz_Vector(a)

    return producto_Matriz(s,b)

def normaVector(a):
    resultado = 0

    for i in range(len(a)):
        for j in range(len(a[0])):
            resultado += a[i][j][0]**2+a[i][j][1]**2

    return math.sqrt(resultado)

def distanciaVector(a,b):

    Resta_vector = resta_vector(a,b)

    for i in range(len(Resta_vector)):
        Resta_vector[i] = [Resta_vector[i]]

    norma_vector = normaVector(Resta_vector)

    return norma_vector

def matrizUnitaria(a):
   
    ope = adjunta_Matriz_Vector(a)
    oper = producto_Matriz(a,ope)

    matriz = [[[1,0] if x == y else [0,0] for y in range(len(a[0]))] for x in range(len(a))]

    for i in range(len(a)):
        for j in range(len(a[0])):
            oper[i][j] = [round(oper[i][j][0]),round(oper[i][j][1])]

    if oper == matriz:
        return True
    else:
        return False

def matrizHermitiana(a):

    ope = adjuntaMatrizVector(a)

    if ope == a:
        return True
    else:
        return False

def productoTensorial_Matriz_Vector(a,b):
    
    matriz = [[[0,0] for column in range(len(a[0])*len(b[0]))] for row in range(len(a)*len(b))]

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = lb.multiplicacion_complejos(a[i // len(b)][j // len(b[0])],b[i % len(b)][j % len(b[0])])


    return matriz
    
