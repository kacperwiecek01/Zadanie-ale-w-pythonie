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

def srednia_ocen():
    try: 
        liczba = int(input("Ile chcesz ocen wprowadzic?"))
        suma = 0

        for i in range (1, liczba + 1):
            while True:

                try:
                    ocena = float(input(f"Podaj ocene {i} od 1 - 6: "))
                    if 1 <= ocena <= 6:
                        suma += ocena
                        break
                    else:
                        print("Ocena musi byc w zakresie 1-6")
                except ValueError:
                        print("Podano nieprawidlowa wartosc")


        srednia = suma / liczba
        print(f"Srednia: {srednia:.2f}")
        
        if srednia >= 3.0:
            print("Uczen zdal")
        else:
            print("Uczen nie zdal")
    except ValueError:
            print("Podano nieprawidlowa liczbe ocen")
def main ():
    while True:
        print("\n--Menu--")
        print("1. Kalkulator")
        print("2. Konwersja temperatury")
        print("3. Srednia ocen")
        print("0. Wyjscie")

        choice = input("Wybierz zadanie: ")

        if choice == "1":
            kalkulator()
        elif choice == "2":
            konwersja_temperatur()
        elif choice == "3":
            srednia_ocen()
        elif choice == "0":
            print ("zamykanie programu...")
            break
        else: 
            print("Nieprawidlowy wybor opcji")
main()