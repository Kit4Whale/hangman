import random


word_list = ["год", "человек", "время",	"дело",	"жизнь", "день", "рука", "работа", "слово", "место", "вопрос", "лицо",
             "глаз", "страна", "друг", "сторона", "дом", "случай", "ребенок", "голова", "система", "вид", "конец",
             "отношение", "город", "часть", "женщина", "проблема", "земля"]

def idiot(letter):
    flag = True
    while flag:
        if len(letter) == 1 and letter.isalpha():
            return letter.upper()
        else:
            print("Введённое значение не валидно. Введите букву: ", end="")
            letter = input()
            flag = False


def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print("Давайте играть в угадайку слов!")

    flag1 = True

    while flag1:  # Основной цикл
        guessed = True
        print(display_hangman(tries))
        print("Слово:", word_completion)
        print("Буква: ", end="")
        letter = idiot(input())

        while guessed:  # Проверка повторов
            if letter in guessed_letters:
                print("Эта буква уже была, введи другую: ", end="")
                letter = idiot(input())
            else:
                guessed_letters.append(letter)
                guessed = False

        if letter in word:  # Проверка наличия буквы и добавление буквы в результат
            if word.count(letter) > 1:
                letter_position1 = word.find(letter)
                letter_position2 = word.rfind(letter)
                word_completion = word_completion[:letter_position1] + letter + word_completion[letter_position1 + 1:]
                word_completion = word_completion[:letter_position2] + letter + word_completion[letter_position2 + 1:]
            else:
                letter_position = word.find(letter)
                word_completion = word_completion[:letter_position] + letter + word_completion[letter_position + 1:]
        else:
            tries -= 1

        for i in range(len(word)):  # Проверка результата
            if word[i] in guessed_letters:
                if i == len(word) - 1:
                    print("Поздравляем, вы угадали слово! Вы победили!")
                    print("Слово:", word_completion)
                    guessed_words.append(word)
                    flag1 = False
                else:
                    continue
            else:
                break

        if tries == 0:  # Проверка ошибок
            print("Гамовир. Загаданное слово было:", word)
            flag1 = False

def flager(answer):
    while True:
        if answer.lower() == "да":
            return True
        if answer.lower() == "нет":
            return False
        else:
            print("Введено не валидное значение")
            print("Укажите (Да/Нет): ", end="")
            answer = input()

flag = True
while flag:
    play(get_word())
    print("Играть ещё? (Да/Нет)")
    flag = flager(input())
