from collections import Counter
import string

ALFABETO = string.ascii_uppercase


def contar_frecuencias(texto):
    letras = [c.upper() for c in texto if c.upper() in ALFABETO]
    total = len(letras)

    if total == 0:
        print("No se encontraron letras.")
        return

    contador = Counter(letras)

    print("\nFrecuencias del texto:\n")

    for letra, cantidad in contador.most_common():
        porcentaje = 100 * cantidad / total
        print(f"{letra}: {cantidad:4} ({porcentaje:5.2f} %)")


def descifrar(texto, sustituciones):
    resultado = ""

    for c in texto:
        mayuscula = c.upper()

        if mayuscula in sustituciones:
            nueva = sustituciones[mayuscula]

            if c.islower():
                nueva = nueva.lower()

            resultado += nueva
        else:
            resultado += c

    return resultado


def mostrar_sustituciones(sustituciones):
    if not sustituciones:
        print("\nNo hay sustituciones definidas.")
        return

    print("\nClave de descifrado (cifrada -> original):")

    for cifrada, clara in sorted(sustituciones.items()):
        print(f"{cifrada} -> {clara}")


def mostrar_clave_cifrado(sustituciones):
    inversa = {
        clara: cifrada
        for cifrada, clara in sustituciones.items()
    }

    print("\nClave de cifrado (original -> cifrada):")

    for original, cifrada in sorted(inversa.items()):
        print(f"{original} -> {cifrada}")


def main():
    print("Ataque por análisis de frecuencias")
    print("Introduce el texto cifrado.")
    print("Termina con una línea vacía.\n")

    lineas = []

    while True:
        linea = input()

        if linea == "":
            break

        lineas.append(linea)

    mensaje = "\n".join(lineas)

    sustituciones = {}

    contar_frecuencias(mensaje)

    while True:
        print("\n" + "=" * 60)
        print(descifrar(mensaje, sustituciones))
        print("=" * 60)

        print("\nOpciones:")
        print("1 - Añadir o cambiar sustitución")
        print("2 - Eliminar sustitución")
        print("3 - Ver frecuencias")
        print("4 - Ver sustituciones")
        print("5 - Finalizar")

        opcion = input("\nOpción: ")

        if opcion == "1":
            cifrada = input("Letra cifrada: ").upper()
            clara = input("Letra original: ").upper()

            if cifrada not in ALFABETO or clara not in ALFABETO:
                print("Debes introducir una letra entre A y Z.")
                continue

            # Evitar que dos letras cifradas correspondan
            # a la misma letra original
            for c, original in sustituciones.items():
                if original == clara and c != cifrada:
                    print(
                        f"La letra {clara} ya está asignada a {c}."
                    )
                    break
            else:
                sustituciones[cifrada] = clara

        elif opcion == "2":
            cifrada = input(
                "Letra cifrada a eliminar: "
            ).upper()

            if cifrada in sustituciones:
                del sustituciones[cifrada]
            else:
                print("Esa sustitución no existe.")

        elif opcion == "3":
            contar_frecuencias(mensaje)

        elif opcion == "4":
            mostrar_sustituciones(sustituciones)

        elif opcion == "5":
            print("\nTEXTO DESCIFRADO:\n")
            print(descifrar(mensaje, sustituciones))

            mostrar_sustituciones(sustituciones)
            mostrar_clave_cifrado(sustituciones)

            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()