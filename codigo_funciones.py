def check_char(x):
    # se define la función check_char
    # con 1 parámetro de entrada
    # dependiendo del tipo de dato y las características
    # de este se retorna un número específico
    # se desarrollan una serie de if's que corroboren las posibles entradas
    if len(str(x)) == 1 and str(x).isalpha():
        # se prueba longitud de entrada menor que 1 y que pertenezca a a-z
        return 0
    elif len(str(x)) > 1 and str(x).isalpha():
        # se prueba longitud de entrada mayor que 1 y que pertenezca a a-z
        return 36
    elif str(x).isalpha() is False and str(x) == x:
        # se prueba que entrada no sea solo caracteres a-z
        # y que se trate solo de caracteres y no otro tipo de dato
        return 1
    else:  # para cualquier otro caso (tipo de dato)
        return 124


def caps_switch(x):
    # se define la función caps_switch con 1 parámetro de entrada
    # dependiendo el tipo de dato que retorne check_char()
    # de ser una única letra a-z lo cambia a mayuscula o
    # minuscula respectivamente, de no ser este el caso entonces
    # devuelve lo mismo que devuelve check_char()
    if check_char(x) != 0:
        # prueba que la entrada no retorne 0
        # si no lo hace devuelve lo mismo que check_char()
        return check_char(x)
    else:  # Para el caso en el que sí retorne 0, modifica la entrada
        if x.isupper():  # corrobora si la entrada es mayuscula
            a = x.lower()  # si sí es mayuscula, la vuelve minuscula
            return a  # retorna la modificación
        elif x.islower():  # corrobora si la entrada es minuscula
            b = x.upper()  # si sí es mayuscula, la vuelve minuscula
            return b  # retorna la modificación
