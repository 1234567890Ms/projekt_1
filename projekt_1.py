"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Michal Slabý
email: michalslaby1@gmail.com => v Engeto založeno pod jakub.rutkowski@allegro.pl
discord: michals._68964
"""

'''
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
'''

import sys

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
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
SEPARATOR = 40 * "-"
USERS = dict(bob="123", ann="pass123", mike="password123", liz="pass123")

titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
sum_numbers = 0
words = 0

def login(users):
    while True:
        username = input("username:").strip()
        password = input("password:")

        # Test hesla
        if username in users.keys() and password == users.get(username, 0):
            print(f"Welcome to the app, {username}")
            break

        else:
            print("unregistered user, terminating the program.")
            # Heslo je nesprávné -> 
            sys.exit()    


def choose_text(text):
    # Počet dostupných textů
    text_count = len(text)
    print(f"We have {text_count} texts to be analyzed.")

    while True:

        select = int(input(f"Enter a number btw. 1 and {text_count} to select:"))

        # Test zadaného čísla výběru
        if select> 0 and select <= text_count:
            break
        else:
            print("Toto číslo je mimo rozsah.")

    return text[select - 1]


def statistics(selected_string):
    text_for_analyze = selected_string.split()
    titlecase = 0
    uppercase = 0
    lowercase = 0
    numeric = 0
    summed = 0

    for word in text_for_analyze:

        word = word.strip(',.')

        if word.istitle():
            titlecase += 1

        elif word.isupper():
            uppercase += 1

        elif word.islower():
            lowercase += 1

        elif word.isnumeric():
            numeric += 1

            summed += int(word)

    # Celkový počet slov v textu
    words = len(text_for_analyze)

    print(f"There are {words} words in the selected text.",
            f"There are {titlecase} titlecase words.",
            f"There are {uppercase} uppercase words.",
            f"There are {lowercase} lowercase words.",
            f"There are {numeric} numeric strings.",
            f"The sum of all the numbers {summed}.",
            sep='\n')  


def histogram(selected_string):
    histogram = dict()
    for words in TEXTS[0].split():
        word = words.strip(',.')
        len_word = len(word)
        histogram[len_word] = histogram.get(len_word, 0) + 1
        sorted_histogram = sorted(histogram)

    for length in sorted_histogram:
        count = histogram[length]
        bar = '*' * count
        print(f'{length:2} |{bar:20}|{count}')


def main():
    print(SEPARATOR)
    login(USERS)
    print(SEPARATOR)
    final_text = choose_text(TEXTS)
    print(SEPARATOR)
    statistics(final_text)
    print(SEPARATOR)
    print('LEN|     OCCURENCES     |NR.')
    print(SEPARATOR)
    histogram(final_text)
    print(SEPARATOR)
    

if __name__ == '__main__':
    main()
