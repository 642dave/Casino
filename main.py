"""
HRA CASINO, STASTNYCH PET
MUJ VLASTNI PROJEKT
AUTHOR: DAVID RAKOVSKY
STUDENT ENGETO ACADEMY
KURZ PYTHON  3.5.2022 - 26.7.2022
DISCORD: #9097
EMAIL: david.rakovsky@centrum.cz

Moje hra KASINO, STASTNYCH PET, je hazardni hra,
kdy muzes vyhrat svoji sazku uhodnutim jednoho z peti cisel

"""

import random

oddelovac = "=" * 60
tvoje_tipovana_cisla = list()
vylosovana_cisla_kasina = list()
tvoje_vyherni_cisla = list()
vyherni_cisla_kasina = list()

print(oddelovac)
print("VITEJ VE HRE CASINO, STASTNYCH PET")
print()
print("""hra KASINO, STASTNYCH PET,je hazardni hra,
kdy muzes vyhrat svoji sazku uhodnutim jednoho z peti cisel
** hru muzes kdykoliv ukoncit napsanim slova konec **""")
print(oddelovac)


def osetri_uzivatelsky_vstup(text):
    # osetri uzivatelsky vstup proti prekliku nebo zadani neplatnych udaju, dale umozni kdykoliv hru ukoncit
    if text.lower() == "konec":
        print("Diky za hru, ukoncuji...")
        quit()
    if not text.isnumeric():
        print("Zadal jsi neplatne udaje, ukoncuji!")
        quit()


while True:
    vklad = input("ZADEJ VKLAD, SE KTERYM JSI OCHOTEN HRAT, max. 20000 $:")
    osetri_uzivatelsky_vstup(vklad)
    print()

    if int(vklad) > 20000:
        print("VYSE TVEHO VKLADU NENI POVOLENA!")
        continue

    if 0 < int(vklad) <= 20000:
        break

while True:

    while True:
        sazka = input(f"ZADEJ SVOJI SAZKU, max. {vklad} $: ")
        osetri_uzivatelsky_vstup(sazka)
        print()

        if int(sazka) > int(vklad):
            print("ZADAL JSI SAZKU, KTERA JE VYSSI NEZ TVUJ AKTUALNI VKLAD!")
            continue

        if 0 < int(sazka) <= int(vklad):
            break

    while True:
        volba_cisla = input("***  Z A D E J  C I S L O  O D  1  D O  5  ***")
        osetri_uzivatelsky_vstup(volba_cisla)
        print()

        if int(volba_cisla) > 5:
            print("ZVOLENE CISLO NENI POVOLENO!")
            print()
            continue

        if 0 < int(volba_cisla) <= 5:
            tvoje_tipovana_cisla.append(volba_cisla)
            break

    print(f"Zadal jsi sazku {sazka} $")
    vylosovane_cislo = random.randint(1, 5)
    print(f"Kasino zadalo sazku {sazka} $")
    print(f"Zvolil jsi cislo {volba_cisla}")
    print(f"Kasino vylosovalo cislo {vylosovane_cislo}")
    vylosovana_cisla_kasina.append(vylosovane_cislo)
    print()

    if vylosovane_cislo == int(volba_cisla):
        tvoje_vyherni_cisla.append(volba_cisla)
        print()
        print("***Gratulujeme, uhodl jsi vylosovane cislo!***")
        print()
        vklad = int(vklad) + int(sazka)
        print(f"Tvuj vklad se navysil o tvoji vyhru {sazka} $")
        print(f"TVOJE TIPOVANA CISLA: {tvoje_tipovana_cisla}")
        print(f"TVOJE VYHERNI CISLA: {tvoje_vyherni_cisla}")
        print(f"VYLOSOVANA CISLA KASINA: {vylosovana_cisla_kasina}")
        print(f"VYHERNI CISLA KASINA: {vyherni_cisla_kasina}")
        print(f"STAV TVEHO KONTA JE AKTUALNE {vklad} $")
        print(oddelovac)

    if vylosovane_cislo != int(volba_cisla):
        vyherni_cisla_kasina.append(vylosovane_cislo)
        print()
        print("---LITUJEME, NEUHODL JSI VYLOSOVANE CISLO!---")
        print()
        vklad = int(vklad) - int(sazka)
        print(f"Tvuj vklad se ponizil o tvoji sazku {sazka} $")
        print(f"Tvoje tipovana cisla: {tvoje_tipovana_cisla}")
        print(f"Tvoje vyherni cisla: {tvoje_vyherni_cisla}")
        print(f"Vylosovana cisla KASINA: {vylosovana_cisla_kasina}")
        print(f"Vyherni cisla KASINA: {vyherni_cisla_kasina}")
        print(f"Stav Tveho konta je aktualne {vklad} $")
        print(oddelovac)

    if int(vklad) == 0:
        print("LITUJEME, ALE NA SVEM KONTE NEMAS JIZ DOSTATEK PROSTREDKU...")
        print(oddelovac)
        print("Nemuzes pokracovat. diky za hru!")
        print(oddelovac)
        break

