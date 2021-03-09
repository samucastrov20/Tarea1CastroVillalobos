# ERR6 -5
import codigo  # Nesesario para importar los modulos


def test_checkcharmay():  # se define la funcion test_checkcharmay
    x1 = 65  # numero que corresponde a "A" en alfabeto ASCII
    while x1 <= 90:  # inicia el ciclo 90 representa la "Z" en alfabeto ASCII
        assert codigo.check_char(chr(x1)) == 0
        # prueba todas las mayusculas en check_char el resultado debe ser 0
        x1 = x1+1  # suma para continuar el ciclo


def test_checkcharmin():  # se define la funcion test_checkcharmin
    x2 = 97  # numero que corresponde a "a" en alfabeto ASCII
    while x2 <= 122:  # inicia el ciclo 122 representa la "z" en alfabeto ASCII
        assert codigo.check_char(chr(x2)) == 0
        # prueba todas las minusculas en check_char el resultado debe ser 0
        x2 = x2+1  # suma para continuar el ciclo


def test_capsswitchmay():  # se define la funcion test_capsswitchmay
    x1 = 65  # numero que corresponde a "A" en alfabeto ASCII
    while x1 <= 90:  # inicia el ciclo 90 representa la "Z" en alfabeto ASCII
        assert codigo.caps_switch(chr(x1)) == chr(x1+32)
        # prueba que todas las mayusculas se tranformen en minusculas
        # el 32 es la diferencia entre las mayus y las minus en ASCII
        x1 = x1+1  # suma para continuar el ciclo


def test_capsswitchmin():  # se define la funcion test_capsswitchmin
    x2 = 97  # numero que corresponde a "a" en alfabeto ASCII
    while x2 <= 122:  # inicia el ciclo 122 representa la "z" en alfabeto ASCII
        assert codigo.caps_switch(chr(x2)) == chr(x2-32)
        # prueba que todas las minusculas se tranformen en mayusculas
        x2 = x2+1  # suma para continuar el ciclo


def test_checkcharlon():
    assert codigo.check_char("aa") == 36  # analisis check_char de longitud


def test_checkcharcarac():
    assert codigo.check_char("%") == 1  # analisis check_char de caracter


def test_checkchardat():
    assert codigo.check_char(3) == 124  # analisis check_char de tipo de dato
