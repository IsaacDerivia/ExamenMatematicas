import webbrowser

def abrir_enlace_dle(palabra):
    """
    Abre el enlace del DLE en el navegador predeterminado con la palabra ingresada.

    Args:
        palabra (str): La palabra a buscar en el diccionario de la RAE.
    """
    url = f"https://dle.rae.es/{palabra}"
    try:
        print(f"Abriendo el enlace: {url}")
        webbrowser.open(url)  # Abre la URL en el navegador predeterminado
    except Exception as e:
        print(f"Error al intentar abrir el navegador: {e}")

# Probar con una palabra
palabra = input("Escribe la palabra para definir: ").strip()
if palabra:
    abrir_enlace_dle(palabra)
else:
    print("No ingresaste ninguna palabra.")
