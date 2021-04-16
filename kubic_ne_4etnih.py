# DZ 2 from pavel mamaev
# make
# 1)a list from 0 to 1000
# 2)make it in a odd numbers
# 3)we need make it in a cube

list_in_2 = [i ** 3 for i in range(1, 1001, 2)]
# print list_in_2

# we have a list, next we need sum of numbers from some elements in our list wich we can divided by 7

sum = 0  # it is our sum of symbols elements wich we can divided by 7
temporary_num = 0  # this is sum our symbol in element

# let's make elements in numbers like string
# now we need make string in 1 symbol

for num_1 in list_in_2:
    temporary_list = list(str(num_1))
    # print(temporary_list)  # test
    temporary_num = 0

        # in each elements we need sum all symbol
    for val_2 in temporary_list:
        temporary_num += int(val_2)
        # print ("val2", val_2)  # test
        # print ("temporary_num", temporary_num)  # test

        # in each elements we need sum all symbol
    if (temporary_num % 7) == 0:
        sum += int(num_1)

    # print ("sum", sum)  # test
print sum, "- is the answer for homework for question 'A'!"

for i in range(len(list_in_2)):
    list_in_2[i] += 17

sum = 0
temporary_num = 0

for num_1 in list_in_2:
    temporary_list = list(str(num_1))
    # print(temporary_list)
    temporary_num = 0

    for val_2 in temporary_list:
        temporary_num += int(val_2)
        # print ("val2", val_2)
        # print ("temporary_num", temporary_num)

    if (temporary_num % 7) == 0:
        sum += int(num_1)

    # print ("sum", sum) #test
print sum, "- is the answer for homework for question 'B'!"
