import random
print('')
print('Witaj graczu! Zostało dla ciebie wylosowane słowo. Masz 11 prób by je zgadnąć. Powodzenia!')
print('')
list_of_words = ["apple", "orange", "strawberry", "perry", "banana"]
word = list_of_words[random.randint(0, len(list_of_words) - 1)]
show_hidden_word = list(word)

for i in range(len(word)):
    show_hidden_word[i] = "_"

lifes = 11
while lifes > 0:
    print("Pozostalo ci ", lifes, " żyć")
    print(" ".join(show_hidden_word))

    print("Podaj swoja litere: ")
    letter = input()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                show_hidden_word[i] = letter
        if "".join(show_hidden_word) == word:
            print("Pozostalo ci ", lifes, " zyc")
            print(" ".join(show_hidden_word))
            print("Gratulacje, wygrałeś!")
            break
    else:
        lifes -= 1
print(f'Koniec gry! Nie udało ci się zgadnąć, hasło to', word)
