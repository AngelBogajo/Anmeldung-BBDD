
print("\n------ Anmeldung BBDD -------")

print("Wilkommen zu unserem Programm")

print("""
1 - Anmelden

2 - Neuer Kunde?
""")
eleccion = input("Geben Sie bitte Option '1' oder '2' ein: -> ")

if eleccion == "1":
    print("OK!, Ich werde brauchen ein paar Daten...")
    input("Geben Sie bitte Ihren Email ein: ")
    input("Geben Sie bitte Ihren Password ein: ")