'''
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Stanislav Šilhán
email: xsils001@gmail.com
discord: Standa.silhan#2772
"""
import ...
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registrovani_uzivatele = {"bob":"123", "ann":"pass123", "mike": "password123", "liz":"pass123"}
oddelovac = 30*"-"

jmeno = input("Username: ")
heslo = input("password: ")

print(oddelovac)

if jmeno in registrovani_uzivatele.keys() and heslo in registrovani_uzivatele.values():
    print("Welcome to the app,", jmeno,
"We have 3 texts to be analyzed.")
else:
    print("unregistered user, terminating the program..")
    exit()

print(oddelovac)

vyber_textu = input("enter a number btw. 1 and 3 to select: ")

if vyber_textu.isalpha():
    print("You choosed wrong number or unknown symbol")
    quit()
elif vyber_textu in (".",",",":","!","@","?"):
    print("You choosed wrong number or unknown symbol")
    quit()
elif int(vyber_textu) in range(1,4):
    next
else:
    print("You choosed wrong number or unknown symbol")
    quit()

print(oddelovac)


for slova in enumerate(TEXTS[int(vyber_textu)-1].split()):
    next
    
# Počet slov výsledek

print("There are", slova[0]+1, "words in the selected text.")

print(oddelovac)

print("LEN|  OCCURENCES  |NR.")

print(oddelovac)


