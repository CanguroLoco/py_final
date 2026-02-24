# Actividad final (entregable)
# Programa: Solicita nombre, edad y estatura; convierte tipos; muestra tamaño en memoria;
# usa constantes y variables; valida identificadores contra palabras reservadas.

import sys
import keyword

# Constantes (convención en mayúsculas)
PROMPT_NOMBRE = "Ingresa tu nombre: "
PROMPT_EDAD = "Ingresa tu edad (en años): "
PROMPT_ESTATURA = "Ingresa tu estatura (en metros, por ejemplo 1.68): "


def calcular_edad(anio_nacimiento: int, anio_actual: int) -> int:
    """Calcula la edad a partir del año de nacimiento y el año actual."""
    return anio_actual - anio_nacimiento

def is_valid_identificator(nombre: str) -> bool:
    """
    Verifica que 'nombre' sea un identificador válido en Python
    y que NO sea palabra reservada.
    """
    return nombre.isidentifier() and not keyword.iskeyword(nombre)

def pedir_entero(mensaje: str) -> int:
    """Solicita un entero y repite hasta que sea válido."""
    while True:
        entrada = input(mensaje).strip()
        try:
            return int(entrada)
        except ValueError:
            print("Entrada no válida. Escribe un número entero (ej. 20).")

def pedir_flotante(mensaje: str) -> float:
    """Solicita un flotante y repite hasta que sea válido."""
    while True:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Entrada no válida. Escribe un número decimal (ej. 1.68).")

def main() -> None:
    print("=== Registro básico (Python + VS Code) ===")

    # 1) Solicitar datos
    nombre = input(PROMPT_NOMBRE).strip()
    edad = pedir_entero(PROMPT_EDAD)
    estatura = pedir_flotante(PROMPT_ESTATURA)

    # 2) Conversiones explícitas (ya convertimos en las funciones, pero se muestran)
    edad_int = int(edad)
    estatura_float = float(estatura)
    nombre_str = str(nombre)

    # 3) Mostrar datos y espacio en memoria
    print("\n--- Datos capturados ---")
    print(f"Nombre   : {nombre_str}")
    print(f"Edad     : {edad_int} años")
    print(f"Estatura : {estatura_float} m")

    print("\n--- Tamaño en memoria (bytes) ---")
    print(f"nombre (str)   -> {sys.getsizeof(nombre_str)} bytes")
    print(f"edad (int)     -> {sys.getsizeof(edad_int)} bytes")
    print(f"estatura (float)-> {sys.getsizeof(estatura_float)} bytes")

    # 4) Ejemplo de variables y constantes
    # Variable calculada
    anio_actual = 2026  # puedes actualizarlo si lo deseas
    anio_nacimiento_aprox = anio_actual - edad_int

    print("\n--- Cálculo con variable y constante ---")
    print(f"Año actual (constante/valor fijo en el programa): {anio_actual}")
    print(f"Año de nacimiento aproximado (variable calculada): {anio_nacimiento_aprox}")

    # 5) Validación de identificadores (evitar palabras reservadas)
    print("\n--- Validación de identificadores ---")
    identificador_propuesto = input(
        "Propón un nombre de variable (identificador) para guardar tu edad: "
    ).strip()

    if is_valid_identificator(identificador_propuesto):
        print(f"✅ '{identificador_propuesto}' es un identificador válido y no es palabra reservada.")
    else:
        if keyword.iskeyword(identificador_propuesto):
            print(f"❌ '{identificador_propuesto}' NO es válido porque es una palabra reservada.")
        elif not identificador_propuesto.isidentifier():
            print(f"❌ '{identificador_propuesto}' NO es válido porque no cumple las reglas de identificador.")
        else:
            print(f"❌ '{identificador_propuesto}' NO es válido por una razón no identificada.")

    print("\nFin del programa.")

if __name__ == "__main__":
    main()




