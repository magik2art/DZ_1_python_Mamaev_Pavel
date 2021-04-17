user_text = int(input("Введите число от 0 до 20 "))
text = ()
i = 0
# for i in range(21): # для проверки
if user_text == 1:
    text = user_text, "Процент"
elif user_text == 2 or user_text == 3 or user_text == 4:
    text = user_text, "Процента"
else:
    text = user_text, "Процентов"
# print(text) # для проверки
    # user_text += 1 # для проверки
print("С числом которое вы ввели ваше склонение будет = ", text)
