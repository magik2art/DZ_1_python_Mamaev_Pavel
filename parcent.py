user_text = int(input("Введите число от 0 до 20 "))
print(user_text)
text = ()
i = 0
for i in range(21):
    if user_text == 1:
        text = (user_text, " Процент")
    elif user_text == 2 or user_text == 3 or user_text == 4:
        text = (user_text, " Процента")
    elif user_text in range(0,21):
       text = (user_text, " Процентов")
    print(text)
    user_text += 1
