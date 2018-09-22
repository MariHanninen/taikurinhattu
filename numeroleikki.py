#Käyttäjä voi arvuutella numeroa, jonka ohjelma arpoo. Koodi on Python harjoittelua.

from random import randint
import sys


def arvaa_numero():
    numero = randint(0, 100)
    while True:

        syote = int(input("Arvaa joku numero 0-100 väliltä: "))
        if syote < 0:
            print("Huono valinta!")
            print("Lopetetaan.")
            sys.exit(0)
        if syote == numero:
            message = "\nArvasit oikein numero on {}!"
            print(message.format(numero))
            break
        elif syote < numero:
            print("Numero on suurempi.")
        else:
            print("Numero on pienempi.")


if __name__ == "__main__":
    arvaa_numero()
