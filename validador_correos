import re
import matplotlib.pyplot as plt

def validar_correo(correo: str) -> bool:
    # Regex básico para validar correos
    regex = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.fullmatch(regex, correo))

def contar_correos(ruta: str) -> dict:
    contador = {"validos": 0, "invalidos": 0}

    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue  # Ignorar líneas vacías

            if "." in linea:
                partes = linea.split(".", 1)  # dividir solo en la primera aparición
                correo = partes[1].strip()
            else:
                correo = linea

            # Contar según validez
            if validar_correo(correo):
                contador["validos"] += 1
            else:
                contador["invalidos"] += 1

    return contador

def graficar_correos(resultado: dict):

    categorias = list(resultado.keys())
    valores = list(resultado.values())

    plt.bar(categorias, valores, color=['green', 'red'])
    plt.title("Cantidad de Correos Válidos e Inválidos")
    plt.ylabel("Número de correos")
    plt.xlabel("Categoría")

    # Mostrar valores encima de cada barra
    for i, v in enumerate(valores):
        plt.text(i, v + max(valores)*0.01, str(v), ha='center', fontweight='bold')

    plt.show()

ruta_archivo = "correos.txt"
resultado = contar_correos(ruta_archivo)

# Graficar
graficar_correos(resultado)
