secret_word = ""
secret_word_list = list(len(secret_word) * "*")
letters_entered = []
commands = {"/help": "Загадано слово. Вы вводите буквы по одной.\
Если Вы угадываете букву, которая есть в слове, то показывается\
загаданное слово и указаваются все отгаданные буквы.\
Если Вы не угадали букву, Вам сообщается, что такой буквы нет.\
Игра продолжается до тех пор, пока не будет угадано слово.",
            "/usedletters": ", ".join(letters_entered),
            "/leftletters": secret_word_list.count("*")}
print(len(secret_word) * "*")
count = 0
while "*" in secret_word_list:
    count += 1
    smth = input()
    if smth == secret_word:
        break
    if smth in commands:
        count -= 1
        print(commands[smth])
        continue
    if smth.isalpha() == False:
        print("Ошибка: вы ввели НЕ букву!")
        continue
    if len(smth) > 1:
        print("Ошибка: вы ввели БОЛЬШЕ одной буквы!")
        continue
    letter = smth
    if letter in letters_entered:
        print("Ошибка: вы уже вводили данную букву!")
        continue
    letters_entered.append(letter)
    commands["/usedletters"] = ", ".join(letters_entered)
    if letter in secret_word:
        print("Есть такая буква!")
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                secret_word_list[i] = letter
        print("".join(secret_word_list))
    else:
        print("Нет такой буквы!")   
print("Поздравляем! Вы угадали слово!")
print(f"Количество затраченных попыток: {count}")
