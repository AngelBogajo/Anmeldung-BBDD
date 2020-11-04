"""

Projekt Registrieren-Login und Mysql:

-> Offen Asistent
-> Login oder Registrieren
-> Wenn Registrieren -> Neuer Kunde in der Datenbank
-> Wenn Login -> Es werden einige Daten fragen
-> Schreiben Notizen, Update Notizen, löschen Notizen, durchschauen Notizen.

Dev- Angel Jesus Bogajo
"""

from user import action   # importar modulo action desde el paquete user


print("\n------ Anmeldung BBDD -------")

print("Wilkommen zu unserem Programm")

print("""
1 - Anmelden

2 - Neuer Kunde?
""")

mach = action.Action() # creando objeto o instanciando mi clase
eleccion = input("Geben Sie bitte Option '1' oder '2' ein: -> ")

if eleccion == "1":
    mach.login()


elif eleccion == "2":
    mach.registrieren()
