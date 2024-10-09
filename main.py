# main.py

def addiere(x, y):
    return x + y


def subtrahiere(x, y):
    return x - y


def multipliziere(x, y):
    return x * y


def dividiere(x, y):
    if y == 0:
        return "Fehler: Division durch Null!"
    return x / y


def main():
    print("Willkommen beim Terminal-Rechner!")
    print("Operationen: ")
    print("1. Addieren")
    print("2. Subtrahieren")
    print("3. Multiplizieren")
    print("4. Dividieren")
    print("Tippe 'exit', um zu beenden.")

    while True:
        wahl = input("Wähle die Operation (1/2/3/4): ")

        if wahl.lower() == 'exit':
            print("Rechner wird beendet. Auf Wiedersehen!")
            break

        if wahl not in ['1', '2', '3', '4']:
            print("Ungültige Eingabe! Bitte wähle eine gültige Operation.")
            continue

        try:
            num1 = float(input("Gib die erste Zahl ein: "))
            num2 = float(input("Gib die zweite Zahl ein: "))
        except ValueError:
            print("Ungültige Eingabe! Bitte gib numerische Werte ein.")
            continue

        if wahl == '1':
            print(f"{num1} + {num2} = {addiere(num1, num2)}")
        elif wahl == '2':
            print(f"{num1} - {num2} = {subtrahiere(num1, num2)}")
        elif wahl == '3':
            print(f"{num1} * {num2} = {multipliziere(num1, num2)}")
        elif wahl == '4':
            ergebnis = dividiere(num1, num2)
            print(f"{num1} / {num2} = {ergebnis}")


if __name__ == "__main__":
    main()
