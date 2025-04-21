def kalkulator():
    try: 
        a = float(input("Podaj pierwsza liczbe: "))
        b = float(input("Podaj druga liczbe: "))
        operacja = input("Wybierz dana operacje:  (+, -, *, /):")

        if operacja == "+":
            wynik = a + b
        elif operacja == "-":
            wynik = a - b
        elif operacja == "*":
            wynik = a * b
        elif operacja == "/":
            if b != 0:
                print (f"Wynik: {a / b}")
            else: 
                print ("Nie mozna dzielic przez zero!")
        else: 
            print("Nieznana operacja")
            return
    except ValueError: 
        print (" Uwaga! Podano nieprawidlowa wartosc.")

def konwersja_temperatur():

    wybor = input("Wybierz kierunek oknwersji (C- Celsujsz -> Fahrenheit, F - Farhenheit -> Celsjusz): ")

    if wybor == "C":
        celsjusz = float(input ("Podaj temperature w C:"))
        Farheneit = celsjusz * 1.8 + 32
        print (f"{celsjusz}C = {Farheneit:.2f}F")
    elif wybor == "F":
        Farheneit = float(input("Podaj temperature w F: "))
        celsjusz = (Farheneit - 32) / 1.8
        print(f"{Farheneit}F = {celsjusz:.2f}C")
    else:
        print("Nieprawidlowy wybor. Wybierz C lub F.")

def main ():
    while True:
        print("\n--Menu--")
        print("1. Kalkulator")
        print("2. Konwersja temperatury")
        print("0. Wyjscie")

        choice = input("Wybierz zadanie: ")

        if choice == "1":
            kalkulator()
        elif choice == "2":
            konwersja_temperatur()
        elif choice == "0":
            print ("zamykanie programu...")
            break
        else: 
            print("Nieprawidlowy wybor opcji")
main()