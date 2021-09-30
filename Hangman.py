"""
Требования:
1) Есть список слов, из которых будет выбираться рандомом(случайным
образом) одно для угадывания.
2) Сразу же будет печататься длина слова знаками "*" 
3) Дальше участнику нужно ввести какую-либо букву и если она есть, то "*"
заменяются на эту букву, а если ее нет, то количество попыток снижается на 1.
Все эти операции будут проходить в цикле while, где условием закрытия
программы будут:

● угадывание слова (победа)
● либо количество попыток == 0.

Например:
● Слово: "Книга"
● Печатается: "*****"
● По мере угадывания появляются буквы: "*нига"
● Также, параллельно принтится количество попыток
"""
import random
words = ["книга", "дом", "ручка", "конкатенация", "очки"]


def Hangman():
    secret = random.choice(words)
    hidden_word = list('*' * len(secret))
    attempts = 5

    while attempts > 0:
        letter = input(f'\n\nУгадайте слово {hidden_word}\nКоличество жизней: {attempts}\nВведите букву: ').lower().strip('')
        if letter == secret:
            print(f"\n\nПоздравляем! Вы угадали слово '{secret.upper()}'")
        if letter in secret:
            for index, value in enumerate(secret):
                if letter == value:
                    hidden_word[index] = letter
            if '*' not in hidden_word:
                print(f'Вы проиграли. Загаданное слово: "{secret.upper()}"')
                break
        else:
            attempts -= 1
            if attempts < 5: print('  | ')
            if attempts < 4: print('  O ')
            if attempts < 3: print(' /|\ ')
            if attempts < 2: print('  | ')
            if attempts < 1: print(' / \ ')
        if attempts == 0:
            print(f'Вы проиграли. Загаданное слово {secret}')
            break

while True:
    playagain = input('Хотите сыграть? (да/нет) ')
    if playagain == 'да':
        Hangman()
    elif playagain == 'нет':
        break
    else:
        print('Введите еще раз')




