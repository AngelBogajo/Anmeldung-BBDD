import user.dieUser as modelo

class Action:

    def registrieren(self): # metodo dentro de la clase
        print("\nOK!, Ich werde brauchen einige Daten...")

        vorname = input("Geben Sie bitte Ihren Vornamen ein: ")
        nachname = input("Geben Sie bitte Ihren Nachnamen ein: ")
        email = input("Geben Sie bitte Ihren Email ein: ")
        password = input("Geben Sie bitte ein Password ein: ")

        user = modelo.User(vorname, nachname, email, password)
        registro = user.registrieren()

        if registro[0] >=1:
            print(f"Ok!, {registro[1].vorname} wurde registriert in der Datenbank mit dem Email{registro[3].email}")

        else:
            print("Fehler: nicht erfolgreiche Registrierung!")


    def login(self): # metodo dentro de la clase
        print("\nOK!, Ich werde brauchen ein paar Daten...")

        email = input("Geben Sie bitte Ihren Email ein: ")
        password = input("Geben Sie bitte Ihren Password ein: ")