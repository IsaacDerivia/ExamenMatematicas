import re  # Librería para trabajar con expresiones regulares, útil para buscar y manipular cadenas de texto.
import random  # Librería para generar números aleatorios y seleccionar elementos aleatoriamente.
from collections import defaultdict  # Librería para crear diccionarios con valores por defecto.
import webbrowser  # Librería para abrir enlaces en el navegador predeterminado.
from symspellpy.symspellpy import SymSpell, Verbosity  # Librería para corrección ortográfica.


# Definición del alfabeto en mayúsculas y minúsculas
alfabeto = [[chr(65 + i) for i in range(26)], [chr(97 + i) for i in range(26)]]

# Diccionarios para almacenar diferentes tipos de palabras
diccionarios = defaultdict(list)

# Lista de colores reconocidos
colores_reconocidos = ["rojo", "verde", "azul", "amarillo", "naranja", "morado", "negro", "blanco", "gris"]


def corregir_palabra(palabra):

    return f"Sugerencia: '{palabra}' podría corregirse como '{palabra[::-1]}' (simulación)."


def abrir_enlace_dle(palabra):
    """
    Abre el enlace del DLE en el navegador predeterminado con la palabra ingresada.
    """
    url = f"https://dle.rae.es/{palabra}"
    try:
        print(f"Abriendo el enlace: {url}")
        webbrowser.open(url)  # Abre la URL en el navegador predeterminado
    except Exception as e:
        print(f"Error al intentar abrir el navegador: {e}")

#inicializar symspell/diccionario de palabras
def inicializar_symspell():
    """
    Configura y carga el diccionario de SymSpell.
    """
    # Inicializar SymSpell
    max_edit_distance = 2  # Número máximo de ediciones permitidas
    prefix_length = 7
    sym_spell = SymSpell(max_edit_distance, prefix_length)

    # Cargar el diccionario de palabras
    dictionary_path = "es_50k.txt"  # Archivo diccionario
    term_index = 0  # La columna 0 contiene las palabras
    count_index = 1  # La columna 1 contiene las frecuencias
    if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
        print("No se pudo cargar el diccionario.")

    return sym_spell


# Inicializar SymSpell
sym_spell = inicializar_symspell()

def corregir_palabra_symspell(palabra):

    # Buscar las mejores coincidencias
    sugerencias = sym_spell.lookup(palabra, Verbosity.CLOSEST, max_edit_distance=2)

    if sugerencias:
        return f"Sugerencias para '{palabra}': {', '.join([s.term for s in sugerencias])}"
    else:
        return f"No se encontraron sugerencias para '{palabra}'."


# Matriz de saludos y frases favoritas
saludos = defaultdict(list)
frases_favoritas = []

# Mensaje de bienvenida personalizado
nombre_usuario = input("Por favor, ingresa tu nombre: ").strip()
print(f"¡Bienvenido al sistema, {nombre_usuario}!")

# Pedir al usuario una frase y asegurarse de que no esté vacía
while True:
    frase = input("Escribe una frase: ").strip()
    if frase:
        break
    else:
        print("La frase no puede estar vacía. Inténtalo de nuevo.")

# Menú principal
while True:
    print("\n--- Menú ---")
    print("1. Ver palabras en los diccionarios")
    print("2. Solicitar definición de una palabra")
    print("3. Corregir una palabra")
    print("4. Registrar un saludo")
    print("5. Usar o ingresar una nueva frase")
    print("6. Elegir aleatoriamente una frase")
    print("7. Agregar frase a favoritos")
    print("8. Ver frases favoritas")
    print("9. Cambiar frase mostrada")
    print("10. Administrar frases (solo administrador)")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Mostrar palabras almacenadas en los diccionarios
        print("\nPalabras almacenadas en diccionarios:")
        for tipo, palabras in diccionarios.items():
            print(f"{tipo.capitalize()}: {palabras}")

    elif opcion == "2":
        # Solicitar definición de una palabra
        palabra = input("Escribe la palabra para definir: ").strip()
        if palabra:
            abrir_enlace_dle(palabra)
        else:
            print("No ingresaste ninguna palabra.")

    elif opcion == "3":
        # Corregir una palabra
        palabra = input("Escribe la palabra a corregir: ").strip()
        print(corregir_palabra_symspell(palabra))

    elif opcion == "4":
        # Registrar un saludo
        momento = input("¿Es un saludo para la mañana, tarde o noche?: ").strip().lower()
        if momento in saludos:
            saludo = input("Escribe el saludo: ").strip()
            saludos[momento].append(saludo)
            print("Saludo registrado.")
        else:
            print("Momento del día no válido.")

    elif opcion == "5":
        # Usar o ingresar una nueva frase
        nueva_frase = input("Escribe una nueva frase o presiona Enter para usar la actual: ").strip()
        if nueva_frase:
            frase = nueva_frase
        print(f"Frase actual: {frase}")

    elif opcion == "6":
        # Elegir aleatoriamente una frase
        if saludos:
            momento = random.choice(list(saludos.keys()))
            saludo_random = random.choice(saludos[momento]) if saludos[momento] else "No hay saludos registrados."
            print(f"Saludo aleatorio ({momento}): {saludo_random}")
        else:
            print("No hay saludos registrados.")

    elif opcion == "7":
        # Agregar frase a favoritos
        frase_favorita = input("Escribe la frase favorita o presiona Enter para usar la actual: ").strip()
        if not frase_favorita:
            frase_favorita = frase
        frases_favoritas.append(frase_favorita)
        print("Frase agregada a favoritos.")

    elif opcion == "8":
        # Ver frases favoritas
        print("\nFrases favoritas:")
        for favorita in frases_favoritas:
            print(favorita)

    elif opcion == "9":
        # Cambiar frase mostrada
        nueva_frase = input("Escribe una nueva frase para guardar: ").strip()
        if nueva_frase:
            frases_favoritas.append(nueva_frase)
            print("Frase agregada sin reemplazar la anterior.")

    elif opcion == "10":
        # Administrar frases (solo administrador)
        rol = input("Escribe tu rol (admin/usuario): ").strip().lower()
        if rol == "admin":
            print("\n--- Administración de Frases ---")
            print("1. Ver todas las frases favoritas")
            print("2. Eliminar una frase favorita")
            print("3. Vaciar todas las frases favoritas")
            admin_opcion = input("Elige una opción: ")

            if admin_opcion == "1":
                # Ver todas las frases favoritas
                print("\nFrases favoritas:")
                for favorita in frases_favoritas:
                    print(favorita)

            elif admin_opcion == "2":
                # Eliminar una frase favorita
                eliminar = input("Escribe la frase a eliminar: ").strip()
                if eliminar in frases_favoritas:
                    frases_favoritas.remove(eliminar)
                    print("Frase eliminada.")
                else:
                    print("Frase no encontrada.")

            elif admin_opcion == "3":
                # Vaciar todas las frases favoritas
                frases_favoritas.clear()
                print("Todas las frases favoritas han sido eliminadas.")
        else:
            print("Acceso denegado. Solo el administrador puede gestionar las frases.")

    elif opcion == "0":
        # Salir del programa
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")
