def input_obligatorio(texto):
    """
    Introduce un valor obligatoriamente (no puede estar vacio).

    Args:
        texto (str): Texto a mostrar para pedir el valor.

    Raises:
        ValueError: Error si el valor esta vacio.

    Returns:
        str: valor escrito
    """
    valor = input(texto)
    if len(valor.strip()) <= 0:
        raise ValueError("Valor incorrecto, Este campo es obligatorio.")
    return valor


def input_int(texto):
    """
    Introduce un valor int (numero entero).

    Args:
        texto (str): Texto a mostrar para pedir el numero.

    Raises:
        ValueError: Error si el numero no es un int.

    Returns:
        str: numero escrito
    """
    try:
        num_int = int(input(texto))
    except ValueError:
        raise ValueError("Valor incorrecto, se necesita un numero entero.")
    else:
        return num_int


def input_float(texto):
    """
    Introduce un valor float (numero decimal).

    Args:
        texto (str): Texto a mostrar para pedir el numero.

    Raises:
        ValueError: Error si el numero no es un float.

    Returns:
        str: numero escrito
    """
    try:
        num_float = float(input(texto))
    except ValueError:
        raise ValueError(
            "Valor incorrecto, se necesita un numero entero o decimal.")
    else:
        return num_float


def val_per(a):
    """
    comprueba si el valor es un texto o numero

    Args:
        a (str): valor

    Returns:
        int, str: int si es un numero si no devuelve str
    """
    try:
        return int(a)
    except ValueError:
        return "NA"


def datos_vacios(name, platform, year, genre, publisher):
    resultado = True
    valor = [name, platform, genre, publisher]
    for datos in valor:
        if len(datos.strip()) <= 0:
            resultado = False
    if not (isinstance(year, int)):
        resultado = False
    if resultado == False:
        raise ValueError("Error, datos obligatorios vacios")
    return resultado


def umbral(vector, corte):
    for valor in vector:
        if valor < corte:
            return False
    return True
