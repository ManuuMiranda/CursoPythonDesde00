"""
Son funciones que añaden funcionalidades a otras funciones, decoran a otras funciones añadiendo funcionalidades.
Estructura: 3 funciones (A, B, C) donde A recibe como parámetro B para devolver C.
Un decorador devuelve una función

def función_decorador_A(función_B):
    def función_interna_C():
         # código de la función_interna_C
    return función_interna_C

Útiles para conectar y cerrar conexión con BBDD por ejemplo

"""


def funcion_decoradora_A(funcion_parametro_B):  # Funcion parametro B será la funcion suma() en este ejemplo

    def funcion_interna_C():
        # Acciones adicionales que decoran/agregan
        print('vamos a realizar un cálculo')
        funcion_parametro_B()
        # Acciones adicionales que decoran/agregan
        print('hemos terminado el calculo')

    return funcion_interna_C()


@funcion_decoradora_A
def suma():
    print(15 + 20)


def resta():
    print(30 - 10)


suma
resta()


################################################################################################################

def funciondecoradora_A(funcionparametro_B):  # Funcion parametro B será la funcion suma() en este ejemplo

    def funcioninterna_C(*args, **kwargs):  # args indica que la función puede recibir un nº indeterminado de parámetros
        # Acciones adicionales que decoran/agregan
        print('vamos a realizar un cálculo')
        funcionparametro_B(*args, **kwargs)  # kwargs para pasar argumentos de tipo clave:valor
        # Acciones adicionales que decoran/agregan
        print('hemos terminado el calculo')

    return funcioninterna_C


@funciondecoradora_A
def sumu(num1, num2, num3):
    print(num1 + num2 + num3)


@funciondecoradora_A
def rest(num1, num2):
    print(num1 - num2)


@funciondecoradora_A
def potencia(base, exponente):
    print(pow(base, exponente))


sumu(7, 5, 8)
rest(12, 10)

potencia(base=5, exponente=3)  # para eso sirve el kwargs, si no no podría hacer la potencia
