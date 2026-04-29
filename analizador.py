import re

def analizar_contrasena(contrasena):
    puntaje = 0
    recomendaciones = []

    # Longitud
    if len(contrasena) >= 12:
        puntaje += 2
    elif len(contrasena) >= 8:
        puntaje += 1
    else:
        recomendaciones.append("Usá al menos 8 caracteres (se recomiendan 12 o más).")

    # Mayúsculas
    if re.search(r'[A-Z]', contrasena):
        puntaje += 1
    else:
        recomendaciones.append("Agregá al menos una letra mayúscula.")

    # Minúsculas
    if re.search(r'[a-z]', contrasena):
        puntaje += 1
    else:
        recomendaciones.append("Agregá al menos una letra minúscula.")

    # Números
    if re.search(r'[0-9]', contrasena):
        puntaje += 1
    else:
        recomendaciones.append("Incluí al menos un número.")

    # Símbolos
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
        puntaje += 2
    else:
        recomendaciones.append("Incluí al menos un símbolo especial (!@#$%...).")

    # Contraseñas comunes
    comunes = ["123456", "password", "qwerty", "abc123", "contraseña", "12345678"]
    if contrasena.lower() in comunes:
        puntaje = 0
        recomendaciones = ["Esta contraseña es extremadamente común. Cambiala inmediatamente."]

    return puntaje, recomendaciones


def nivel_fortaleza(puntaje):
    if puntaje <= 1:
        return "MUY DÉBIL 🔴"
    elif puntaje <= 3:
        return "DÉBIL 🟠"
    elif puntaje <= 5:
        return "MODERADA 🟡"
    elif puntaje == 6:
        return "FUERTE 🟢"
    else:
        return "MUY FUERTE 💪"


def main():
    print("=" * 45)
    print("   ANALIZADOR DE FORTALEZA DE CONTRASEÑAS")
    print("=" * 45)

    while True:
        contrasena = input("\nIngresá una contraseña (o 'salir' para terminar): ")

        if contrasena.lower() == "salir":
            print("\nHasta luego!")
            break

        puntaje, recomendaciones = analizar_contrasena(contrasena)
        nivel = nivel_fortaleza(puntaje)

        print(f"\nPuntaje: {puntaje}/7")
        print(f"Fortaleza: {nivel}")

        if recomendaciones:
            print("\nRecomendaciones:")
            for r in recomendaciones:
                print(f"  → {r}")
        else:
            print("\n✅ ¡Tu contraseña es muy sólida!")

        print("-" * 45)


if __name__ == "__main__":
    main()
