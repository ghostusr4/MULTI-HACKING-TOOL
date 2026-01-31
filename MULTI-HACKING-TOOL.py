import os
import sys
import subprocess

def passwort_knacken(passwort_hash):
    print("Knacke das Passwort...")
    # Hier füge deinen Code zum Knacken von Passwörtern ein

def ddos_ziel_ip(ip):
    print("Starte DDoS-Angriff auf die IP: " + ip)
    # Hier füge deinen Code für einen DDoS-Angriff ein

def dateien_verschlüsseln(ordner):
    print("Verschlüssele alle Dateien im Ordner: " + ordner)
    # Hier füge deinen Code zum Verschlüsseln von Dateien ein

def zeige_menu():
    print("### MULTI-HACKING-TOOL MENU ###")
    print("1. Passwort knacken")
    print("2. DDoS-Angriff starten")
    print("3. Dateien verschlüsseln")
    print("4. Exit")

def main():
    while True:
        zeige_menu()
        option = input("Wähle eine Option: ")

        if option == "1":
            passwort_hash = input("Gib das Passwort-Hash ein: ")
            passwort_knacken(passwort_hash)
        elif option == "2":
            ip = input("Gib die Ziel-IP für den DDoS-Angriff ein: ")
            ddos_ziel_ip(ip)
        elif option == "3":
            ordner = input("Gib den Ordnerpfad zum Verschlüsseln ein: ")
            dateien_verschlüsseln(ordner)
        elif option == "4":
            print("Auf Wiedersehen, mein Meister!")
            break
        else:
            print("Ungültige Option. Bitte wähle eine gültige Option.")

if __name__ == '__main__':
    main()