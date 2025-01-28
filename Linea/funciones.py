'''
    Funciones auxiliares para el programa "Linea"
'''

def calcular_y(x,m,b):
    '''
        Calcula "y" de acuerdo a la pendiente "m" y el punto de intersección en y "b"
        Retorna el valor de "y"
    '''

    return m*x+b

if __name__ == "_main_":
    x = 0
    m = 3
    b = 2
    y = calcular_y(x,m,b)
    if y== 2:
        print("Prueba Exitosa")
    else:
        print("Prueba Fallida")
