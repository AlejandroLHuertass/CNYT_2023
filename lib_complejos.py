import math
# Alejandro L. Huertas

# Libreria para operaciones entre numeros complejos
   
def suma_complejos(x,y):
    a = x[0] + y[0]
    b = x[1] + y[1]

    return (a,b)

def multiplicacion_complejos(x,y):
    a = x[0] * y[0] - x[1] * y[1]
    b = x[0] * y[1] + x[1] * y[0]

    return(a,b)

def resta_complejos(x,y):
    a = x[0] - y[0]
    b = x[1] - y[1]

    return (a,b)

def division_complejos(x,y):
    a = ((x[0]*y[0]) + (x[1]*y[1]))/((y[0]**2)+(y[1]**2))
    b = ((x[1]*y[0]) - (x[0]*y[1]))/((y[0]**2)+(y[1]**2))

    return(a,b)


def modulo_complejos(x):
    c = ((x[0]**2)+(x[1]**2))**(1/2)
    
    return c


def conjugado_complejos(x):
    
    return (x[0],x[1]*-1)
 


def cartesiano_polar_complejos(x):
    angulo = math.degrees(math.atan2(x[1], x[0]))
    r = math.sqrt((x[0]**2) + (x[1]**2))
    
    return [r, angulo]


def polar_cartesiano_complejos(x):

    r = x[0]
    angulo = math.radians(x[1])
    a = r * math.cos(angulo)
    b = r * math.sin(angulo)
    return [a, b]


def fase_complejos(x):
    c = math.degrees(math.atan2(x[1], x[0]))

    return c








