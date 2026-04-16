
def fibonacci(fibonacci_number):
    # Validación de tipo
    if not isinstance(fibonacci_number, int):
        raise ValueError("El valor debe ser un número entero")

    # Validación de rango
    if fibonacci_number < 0:
        raise ValueError("El valor no puede ser menor que cero")

    # Casos base
    if fibonacci_number == 0:
        return 0
    if fibonacci_number == 1:
        return 1

    # Cálculo iterativo
    a, b = 0, 1
    for _ in range(2, fibonacci_number + 1):
        a, b = b, a + b

    return b


