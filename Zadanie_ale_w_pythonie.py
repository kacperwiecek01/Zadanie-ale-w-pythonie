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
            if b == 0:
                print ("Uwaga! Nie mozna dzielic przez zero!")
                return
            wynik = a / b
        else: 
            print("Nieznana operacja")
            return
        
        print (f"wynik: {wynik}")
    except ValuveError: 
        print (" Uwaga! Podano nieprawidlowa wartosc.")
kalkulator ()