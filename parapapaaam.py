print("Добро пожаловать в квиз по анатомии человека!    ~Медики должны всё знать:)~")
print("\nОтветь на следующие вопросы:\n")
questions= ("Сколько костей у взрослого человека?", "Сколько примерно раз в минуту сокрощается наше сердце?",
            "Какая самая большая клетка в человеческом теле?", "Из скольки различных костей состоит череп?",
            "Как вы думаете с какой скоростью двигается нервный импульс из мозга? Напишите ответ в км/ч",
            "Какая единственная часть тела, которая не имеет кровоснабжения?",
            "Скажите, сколько клеток в вашем теле отмирают и заменяются на новые в то время, как вы читаете этот вопрос?",
            "Как вы думаете, правда ли то, что, женские сердца бьются быстрее, чем у мужчин?",
            "Сколько процентов снов забывает человек?")
answers=[207, 70, "яйцеклетка", 29, 274, "роговица", 50000,"да", 98 ]
Balls=0

print(f"1. {questions[0]}")
answer1=int(input("Ваш ответ:"))
if answer1==answers[0]:
    print("Ты молодец, за это я дам тебе 3 балла")
    Balls=Balls+3
else:
    print(f"ну как так то,правильный ответ: {answers[0]}")
    Balls=Balls-1

print(f"2.{questions[1]}")
answer2=int(input("Ваш ответ:"))
if answer2==answers[1]:
    print("На тебе +3 балла")
    Balls=Balls+3
else:
    print(f"ну как так то,правильный ответ: {answers[1]}")
    Balls=Balls-1

print(f"3.{questions[2]}")
answer3=(input("Ваш ответ:"))
if answer3.lower()==answers[2]:
    print("+3 балла")
    Balls=Balls+3
else:
    print(f"ну как так то, правильный ответ: {answers[2]}")
    Balls=Balls-1

print(f"4.{questions[3]}")
answer4=int(input("Ваш ответ:"))
if answer4==answers[3]:
    print("Ну ладно, я поверю что ты умный, +3 балла")
    Balls=Balls+3
else:
    print(f"ну как так то, правильный ответ: {answers[3]}")
    Balls=Balls-1

print(f"5.{questions[4]}")
answer5=(input("Ваш ответ:"))
if answer5==answers[4]:
    print("Ухх, молодец, +3 балла")
    Balls=Balls+3
else:
    print(f"ну как так то, правильный ответ: {answers[4]}")
    Balls=Balls-1

print(f"6.{questions[5]}")
answer6=(input("Ваш ответ:"))
if answer6.lower()==answers[5]:
    print("+3 балла тебе в копилку")
    Balls=Balls+3
else:
    print(f"ну как так то, правильный ответ: {answers[5]}")
    Balls=Balls-1

print(f"7.{questions[6]}")
answer7=int(input("Ваш ответ:"))
if answer7==answers[6]:
    print("+3 балла")
    Balls=Balls+3
else:
    print(f"Ну ващее, правильный ответ: {answers[6]}")
    Balls=Balls-1

print(f"8.{questions[7]}")
answer8=(input("Ваш ответ:"))
if answer8.lower()==answers[7]:
    print("+3 балла")
    Balls=Balls+3
else:
    print(f"ну как так то, правильный ответ: {answers[7]}")
    Balls=Balls-1


print(f"9.{questions[8]}")
answer9=int((input("Ваш ответ:")))
if answer9==answers[8]:
    print("+3 балла")
    Balls=Balls+3
else:
    print(f"ну как так то, правильный ответ: {answers[8]}")
    Balls=Balls-1

if Balls==27:
    print("Да ты прям вундеркинд, поздравляю, у тебя 27 баллов из 27 возможных")
if Balls<=0:
    print(f"эх, у тебя {Balls} баллов, но не растраивайся ♥")
if 0<Balls<27:
    print(f"ВАААУ, ты большой молодец у тебя {Balls} баллов из 27 возможных!")