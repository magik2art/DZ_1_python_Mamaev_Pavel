# -*- coding: utf-8 -*-
# К сожалению не смог подключить UTF-8 и кириллицу не отоброжает, поэтому просклонять не удалось - в папке лежит скриншот
user_text = int(input("Введите число от 0 до 20 "))
print user_text
text = ()
# for test1 in range(21):
i = 0
for i in range(21):
    if user_text == 1:
        text = (user_text, " Procent") # Процент
    elif user_text == 2 or user_text == 3 or user_text == 4:
        text = (user_text, " Procent'a") # Процента
    elif user_text in range(0,20):
       text = (user_text, " Procent'ov") # Процентов
    print text
    user_text += 1