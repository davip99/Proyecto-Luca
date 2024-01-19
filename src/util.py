def input_obligatorio(texto):
    valor = input(texto)
    if len(valor.strip()) <= 0:
        raise ValueError("Valor incorrecto, Este campo es obligatorio.")
    return valor


def input_int(texto):
    try:
        num_int = int(input(texto))
    except ValueError:
        raise ValueError("Valor incorrecto, se necesita un numero entero.")
    else:
        return num_int


def input_float(texto):
    try:
        num_float = float(input(texto))
    except ValueError:
        raise ValueError(
            "Valor no correcto, se necesita un numero entero o decimal.")
    else:
        return num_float


def val_per(a):
    try:
        return int(a)
    except ValueError:
        return "NA"
