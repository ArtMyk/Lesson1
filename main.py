# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# number3 = int(input("Enter third number: "))
#
#
# addition = number1 + number2 + number3
# print (f"number1: {number1} number2: {number2} number3: {number3}")
# print (f"Addition: {addition}")
#
#
# multiplication = number1 * number2 * number3
# print (f"number1: {number1} number2: {number2} number3: {number3}")
# print (f"Multiplication: {multiplication}")
#
#
# lengthAB = int(input("Enter first number: "))
# lengthCD = int(input("Enter second number: "))
# area = ((lengthAB * lengthCD)/2)
# print (f"lengthAB: {lengthAB} lengthCD: {lengthCD}")
# print (f"area: {area}")
#
# number = input("Enter for digit number: ")
#
# multiplication = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
# print (f"multiplication_number", multiplication)

#################################################

# n1, n2 = 10, 20
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)

##############################################

# hours = int(input("Enter hours:"))
#
# if hours >= 12 and hours <= 23:
#     print("PM")
# elif hours >= 0 and hours < 12:
#     print("AM")
# else:
#     print("Incorrect hours!")

################################################

# film_rating = int(input("Enter film rating:"))
#
# if film_rating >0 and film_rating <= 5:
#     if film_rating == 4 or film_rating == 5:
#         print("OK!")
#     else:
#         print("Not OK!")
# else:
#     print ("Incorrect rating!")

###############################################
#
# number = int(input("Enter three digits: "))
# n1 = number // 100
# n2 = number // 10 % 10
# n3 = number % 10
#
# biggest = n1 >= n2 and n1 >= n3
# smallest = n1 <= n2 and n1 <= n3
# arithmetic_mean = (n1 + n2 + n3) / 3
#
# biggest_calculating = 1
# smallest_calculating = 2
# arithmetic_mean_calculating = 3
#
# print("task #: 1 biggest_calculating, 2 smallest_calculating 3 arithmetic_mean_calculating")
#
# task = int(input("Enter task: "))
#
# if task > 0 and task <= 3:
#
#     if 1 == biggest_calculating:
#         if task == biggest_calculating:
#             if n1 >= n2 and n1 >= n3:
#                 print(f"biggest: {n1}")
#
#             elif n2 >= n1 and n2 >= n3:
#                 print(f"biggest: {n2}")
#
#             elif n3 >= n2 and n3 >= n1:
#                 print(f"biggest: {n3}")
#
#     if 2 == smallest_calculating:
#         if task == smallest_calculating:
#             if n1 <= n2 and n1 <= n3:
#                 print(f"smallest: {n1}")
#
#             elif n2 < n1 and n2 < n3:
#                 print(f"smallest: {n2}")
#
#             elif n3 < n1 and n3 < n3:
#                 print(f"smallest: {n3}")
#
#     if task == arithmetic_mean_calculating:
#         print(f"arithmetic_mean: {arithmetic_mean}")
# else:
#     print("Incorrect task number!")

#################################################

# number = int(input("Enter meters: "))
#
# meters = number
#
# meters_to_miles = meters / 1609.344
# meters_to_yards = meters * 1.09361
# meters_to_inches = meters * 39.3701
#
# meters_to_miles_calculating = 1
# meters_to_yards_calculating = 2
# meters_to_miles_mean_calculating = 3
#
# print("task #: 1 meters_to_miles_calculating, 2 meters_to_miles_calculating 3 meters_to_miles_mean_calculating")
#
# task = int(input("Enter task: "))
#
# if task > 0 and task <= 3:
#
#     if 1 == meters_to_miles_calculating:
#         if task == meters_to_miles_calculating:
#             print(f"meters_to_miles_calculating: {meters_to_miles}")
#
#     if 2 == meters_to_yards_calculating:
#         if task == meters_to_yards_calculating:
#             print(f"meters_to_miles_calculating: {meters_to_yards}")
#     if 3 == meters_to_miles_mean_calculating:
#         if task == meters_to_miles_mean_calculating:
#             print(f"meters_to_miles_mean_calculating: {meters_to_inches}")
# else:
#     print("Incorrect task number!")

#####################################################################

# number = int(input("Enter three digits: "))
#
# n1 = number // 100
# n2 = number // 10 % 10
# n3 = number % 10
#
# print (f"n1: {n1} n2: {n2} n3: {n3}")
#
# if n1 == n2 == n3:
#         print("number of equals: 3")
#
# elif n1 == n2 or n1 == n3 or n2 == n3:
#     print("number of equals: 2")
#
#######################################
#
# n1, n2 = 10, 1
# print(n1 / n2)
#
# num = float(input("Enter the number"))
# print(num)
# print(int(num))
#
########################################
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     result = num1 / num2
#
#     print(f"Result: {result}")
# except ZeroDivisionError as error:
#     print(f"ZeroDivisionError occurred: {error}")
# except ValueError as error:
#     print("Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except Exception as error:
#     print(f"Exception occurred: {error}")
# finally:
#     print("End of calculation")
#
# print("some text")\
#
# ################################################
# try:
#     name = input("Enter you name")
#
#     if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#     else:
#         raise Exception("Please enter a valid name!")
# except Exception as e:
#     print(f"Error: {e}")
#
###########################################
# try:
#     print("1. Start game\n2. Settings\n3. Saved games\n4. Exit")
#     user_select = int(input("Enter menu number: "))
#
#     if user_select == 1:
#         print("Game started")
#     elif user_select == 2:
#         print("Settings opened")
#     elif user_select == 3:
#         print("Saved games opened")
#     elif user_select == 4:
#         print("Exit...")
#     else:
#         print("Incorrect menu item!")
#
#     match user_select:
#         case 1:
#             print("Game started")
#         case 2:
#             print("Settings opened")
#         case 3:
#             print("Saved games opened")
#         case 4:
#             print("Exit...")
#         case _:
#             print("Incorrect manu item!")
#
# except Exception as e:
#     print(f"Error: {e}")
#
##################################################
#
# try:
#     num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))
#     result = num1 / num2
# except Exception as error:
#     print(error)
#
# print("Hello")
#
###################################
#
# i = 0
#
# while True :
#
#     if i == 5:
#         i += 1
#         print("continue...")
#         continue
#
#     if i > 10:
#         print("break...")
#         break
#
#     print(i)
#
#     i += 1
#
# print("hello")
#
########################################################
# #
# sum_nums = 0
# count = 0
#
# try:
#     while True:
#         num = int(input("Enter number: "))
#
#         if num == 0:
#             print("end...")
#             break
#
#         sum_nums += num
#         count += 1
#
#     average = sum_nums / count
#     print(f"sum_nums: {sum_nums}")
#     print(f"count: {count}")
#     print(f"average: {average}")
# except ValueError as e:
#     print("Enter numbers only")
# except Exception as e:
#     print(e)

#############################################################
#
# for i in range(3):
#
#     print(i, end=" ")
#
# print()
#
# for i in range(2, 5):
#
#     print(i, end=" ")
#
# print()
#
# for i in range(1, 6, 2):
#
#     print(i, end=" ")
#
# start, end = 1, 10
# for i in range(start, end + 1):
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(end, start -1, -2):
#
#     print(i, end=" ")
#
###############################################################
#
# for  value in 1, 4, "adsd", True, "sdfsdfsdf":0
#     print(value)
#
############################################################
#
# start = int(input("Enter start value "))
# end = int(input("Enter end value: "))
#
# if start > end:
#     start, end = end, start
#
#
# if start > end:
#     temp = start
#     start = end
#     end = temp
#
# for number in range(start, end + 1):
#     is_simple = True
#
#     if number < 2:
#         continue
#
#     for i in range(2, number):
#         if number % i == 0:
#             is_simple = False
#             break
#
#     if is_simple:
#         print(number, end=" ")

#################################################
#
# message = "hello world"
# message_1 = 'hello world'
# print(message)
#
# text = "hello" \
#         "world"
# print(text)
#
############################
# text = '''
# qwerty
#     asdsvf
#         asdfsdf
# '''
#
# print(text)
#
# path = r"C:\Users\admin\PycharmProjects\FastAPI_materials"
# print(path)
#
# path = "C:\\Users\\admin\\PycharmProjects\\FastAPI_materials"
# print(path)
#
###############################
#
# print("hello, \"world\"\n\from program")
#
###############################
# dogs, cats = 12, 15
# result = f"Dogs {dogs} and cats {cats}"
# print (result)

# text = "Dogs {} and cats {}"
# result = text.format(dogs,cats)
# print(result)

# result = "Dogs {1} and cats {0}".format (dogs, cats )
# print(result)
#
# result = "Dogs {1} and cats {1}".format(dogs, cats)
# print(result)
#
###############################
#
# message = "hello world"
#
# print(message[0])
# print(len(message))
# print(message[len(message) - 1])
# print(message[-3])
#
###############################
#
# name ="Petya"
# print(name)
#
# user_name = "Vasia"
# name = user_name
# print(name)
#
# ###############################

# sentence = "Hello, world"
# # for letter in sentence:
# #     print(letter, end=" ")
# #
# # print()
#
# for i in range(len(sentence)):
#     print(sentence[i], end=" ")
#
# # ###############################
#
# sentence = "Hello world"
# print(sentence[:])
# print(sentence[0:])
# print(sentence[2:])
# print(sentence[2:8])
# print(sentence[1:10:2])
# print(sentence[::-1])
#
# ###############################
#
# name = "Vasya"
# surname = "Petrov"
# age = 33
#
# fullname = name + " " + surname + " " + str(age)
# print(fullname)
#
# ###############################
#
# text = "Hello, world" * 3
# print(text)
#
# print("------" * 10)
#
# ###############################
#
# a1 = "abc"
# a2 = "abs"
#
# if a1 > a2:
#     print(a1)
# else:
#     print(a2)
#
# print(ord("A"))
# print(chr(98))
#
################################## 21.01.2024
#
# num = 20
#
# match num:
#     case 1:
#         prin()
#     case 2:
#         print()
#     case _:
#         print()
#
# text = "hello world. goodbye world."
# search_item = ". "
# current_index = text. find(search_item)
#
# first_sentence = text[:current_index + len(search_item)]
# second_sentence = text[current_index + len(search_item):]
#
# final_sentence = first_sentence.capitalize() + second_sentence.capitalize()
# print(final_sentence)
#
# print(text.count("."))
#
# symbol = "* "

# v1
# for i in range (1, 6):
#     print(symbol * i)

# v2
# counter = 1
#
# for i in range(5):
#     for j in range(counter):
#         print(symbol, end="")
#     print()
#     counter += 1

# for i in range(5):
#     if i == 0 or i == 4:
#         for j in range(5):
#             print(symbol, end="")
#     else:
#         print(symbol, end="")
#         for j in range(3):
#             print("  ", end="")
#         print(symbol, end="")
#     print()
#
# stars_count = 5
# whitespace_count = 0

# for i in range(5):
#     for j in  range(whitespace_count):
#         print("  ", end="")
#
#     for j in range(stars_count):
#         print(symbol, end="")
#
#     for j in range(whitespace_count):
#         print("  ", end="")
#
#     if i < 2:
#         stars_count -= 2
#         whitespace_count += 1
#     else:
#         stars_count += 2
#         whitespace_count -= 1
#     print()
#
# numbers = []
# numbers_1 = list()
# print(type(numbers))
# print(type(numbers_1))
#
# numbers = [1, 3, 25, 7, 2, 7]
#
# print(numbers)
# print(numbers[0])
#
# numbers[2] = 11111
# print(numbers)
# print(len(numbers))
# print(numbers[-1])
#
# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
#
# print()
#
# for number in numbers:
#     print(number, end=" ")
#
# print()
# value = ["one", 12, 12.4, True]
# print(value)
#
# nums = [1, 3] * 5
# print(nums)
#
# numbers = [1, 3, 25, 7, 2, 7]
#
# print(numbers[:])
# print(numbers[1:5])
# print(numbers[1:5:2])
# print(numbers[::-1])
#
# users = ["Vasya", "Petya", "Kolya"]
# user_1, user_2, user_3 = users
# user_1, user_2, user_3 = users[0], users[1], users[2]
# print(user_1)
# print(user_2)
# print(user_3)
# print(users)

# import random
#
# print(random.randint(1, 10))
# NUM_SIZE = 10
# numbers = []
#
# for i in range(NUM_SIZE):
#     numbers.append(random.randint(1, 10))
#
# print(numbers)

# #append(item): додає елемент item до кінця списку
#
# numbers.append(2222)
# print(numbers)
#
# #insert(index, item): додає елемент item до списку за індексом index
#
# numbers.insert(1, 3333)
# print(numbers)
#
# #extend(items): додає набір елементів items до кінця списку
#
# numbers.extend([2, 3, 4])
# print(numbers)
#
# numbers += [1, 2, 3, 4]
# print(numbers)
# #
# # remove(item): видаляє елемент item. Видаляється лише перше входження елемента.
# # Якщо елеменит не знайдено, генерує виняток ValueError
# #
# numbers.remove(2222)
# print(numbers)
# #
# # clear(): видалення всіх елементів зі списку
# #
# numbers.clear()
# print(numbers)
#
# del numbers # видаляє змінну
# print(numbers)
## index(item):повертає індекс елемента item. Якщо елемент не знайдено, генерує виняток ValueError
#
# print(numbers.index(2))
# print(numbers)
#
# # pop([index]): видаляє та повертає елемент за індексом index.
# result = numbers.pop()
# print(result)
# print(numbers)
## count(item): повертає кількість входжень елемента item до списку
##
# print(numbers.count(1))
#
# v1
# numbers.sort()
# print(numbers)
# # v2
# numbers_sorted = sorted(numbers)
# print(numbers_sorted)
# print(numbers)
#
# people = ["Tom", "bob", "alice", "Sam", "Bill"]
# # v1
# # people.sort()
# # print(people)
# # v2
# # people.sort(key=str.lower)
# # print(people)
# ##
# people_sorted = sorted(people, key=str.lower)
# print(people_sorted)
# print(people)

# reverse(): розставляє всі елементи у списку у зворотньому порядку

# numbers.reverse()
# print(numbers)

# copy(): копіює список
#
# nums_1 = [1, 3, 5]
# nums_copy = nums_1.copy()
# print(nums_1)
# print(nums_copy)
# nums_copy[1] = 1111
# print(nums_1)
# print(nums_copy)

# #len(list): повертає довжину списку
#
# print(len(numbers))
#
# # min(list): повертає найменший елемент списку
#
# print(min(numbers))
#
# # max(list): повертає найбільший елемент списку
#
# print(max(numbers))

###############
# text = "hello world. goodbye world."
# search_item = ". "
#
# sentences = text.split(search_item)
# print(sentences)
#
# result = []
#
# for sentence in sentences:
#     result.append(sentence.capitalize())
#
# print(result)
#
# result_sentence = search_item.join(result)
# print(result_sentence)

##
# створити список із 10 випадкових чисел
# поміняти місцями мінімальне значення з максимальним
# [3, 1, 4, 2, 5] -> [3, 5, 4, 2, 1]
#
# numbers = [3, 1, 4, 2, 5]

# v1
# print(numbers)
#
# min_value = min(numbers)
# max_value = max(numbers)
#
# min_value_index = numbers.index(min_value)
# max_value_index = numbers.index(max_value)
#
# numbers[min_value_index] = max_value
# numbers[max_value_index] = min_value
#
# print(numbers)

# v2

# numbers_copy = numbers.copy()
#
# print(numbers)
#
# numbers_copy[numbers.index(min(numbers))], numbers_copy[numbers.index(max(numbers))] = max(numbers), min(numbers)
# numbers = numbers_copy.copy()
# print(numbers)
#

# problem
# numbers[numbers.index(min(numbers))], numbers[numbers.index(max(numbers))] = 111, 222
# numbers[numbers.index(min(numbers))] = 111
# numbers[numbers.index(max(numbers))] = 222

# print(numbers)

###############
# numbers = ["Vasya", 33, ["dance", "walk"]]
# print(numbers)
# print(numbers[2])
# print(numbers[2][0])

##
# v1
# array = [
#     [1, 3, 2],
#     [1, 4],
#     1,
#     [
#         [1, 2],
#         [3, 5]
#     ]
# ]
# print(array)
# print(array[3][1][1])
# print(array[3][0][0])
# v2
# matrix = [
#     [24, 41, 15, 62],
#     [22, 41, 15, 62],
#     [25, 42, 11, 66],
#     [27, 46, 16, 63]
# ]

# print(matrix[0][1])
# #
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

#
# import random
#
# matrix = []
#
# print(matrix)
# for i in range(10):
#     matrix.append([])
#     for j in range(10):
#         matrix[i].append(random.randint(10, 99))
#
# print(matrix)
#
# v1
# print(len(matrix))
# print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
#
# print()
# # # v2
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()
#
#
################################# Homework 5 - 1
#
# import random
#
# NUM_SIZE = 10
# numbers = []
#
# for i in range(NUM_SIZE):
#     numbers.append(random.randint(-10, 10))
#
# print(numbers)
#
# sum_of_negative_numbers = 0
#
# for j in range(NUM_SIZE):
#     if numbers[j] < 0:
#         sum_of_negative_numbers += numbers[j]
#
# print("Sum of negative numbers: ", sum_of_negative_numbers)
#
# sum_of_even_numbers = 0
#
# for j in range(NUM_SIZE):
#     if numbers[j]%2 == 0:
#         sum_of_even_numbers += numbers[j]
# print("Sum of even numbers: ", sum_of_even_numbers)
#
# sum_of_odd_numbers = 0
#
# for j in range(NUM_SIZE):
#     if numbers[j]%2 != 0:
#         sum_of_odd_numbers += numbers[j]
#
# print("Sum of odd numbers: ", sum_of_odd_numbers)
#
# sum_of_odd_numbers = 0
#
# for j in range(NUM_SIZE):
#     if numbers[j]%2 == 0:
#         sum_of_odd_numbers += numbers[j]
#
# print("Sum of odd numbers: ", sum_of_odd_numbers)
#
# sum_of_elements_with_multiple_of_3 = 0
# for i in range(len(numbers)):
#     if i % 3 == 0:
#         sum_of_elements_with_multiple_of_3 += numbers[i]
#
# print("Sum of elements with multiple of 3:", sum_of_elements_with_multiple_of_3)
#
# min_index = numbers.index(min(numbers))
# max_index = numbers.index(max(numbers))
#
# if min_index > max_index:
#     min_index, max_index = max_index, min_index
#
# sum_btw_min_and_max_index = 0
# for i in range(min_index + 1, max_index):
#     sum_btw_min_and_max_index += numbers[i]
#
# print("Sum btw min and max index: ", sum_btw_min_and_max_index)
#
# first_positive_index = last_positive_index = 0
# for i in range(NUM_SIZE):
#     if numbers[i] > 0:
#         first_positive_index = i
#         break
#
# for i in range(NUM_SIZE -1, -1, -1):
#     if numbers[i] > 0:
#         last_positive_index = i
#         break
#
# print(first_positive_index, last_positive_index)
#
# sum_btw_first_and_last_positive_elements = 0
# for i in range(first_positive_index +1, last_positive_index):
#     sum_btw_first_and_last_positive_elements = numbers[i]
#
# print("Sum btw first and last positive elements: ", sum_btw_first_and_last_positive_elements)
#
# ######################################### Homework 5-2
#
# import random
#
# NUM_SIZE = 10
# numbers = []
#
# for i in range(NUM_SIZE):
#     numbers.append(random.randint(-10, 10))
#
# print(numbers)
#
# numbers_even = [j for j in numbers if j % 2 == 0]
#
# print(numbers_even)
#
# numbers_odd = [j for j in numbers if j % 2 != 0]
#
# print(numbers_odd)
#
# nums_negative = [j for j in numbers if j < 0]
#
# print(nums_negative)
#
# nums_positive = [j for j in numbers if j > 0]
#
# print(nums_positive)

############################################################################################################################################################################# 24.02.2024

# У списку цілих, заповненому випадковими числами обчислити:
# import random
# # numbers = []
# ARR_SIZE = 10
# v1
# for _ in range(ARR_SIZE):
#     numbers.append(random.randint(-10, 10))
# v2
# numbers = [random.randint(-10, 10) for i in range(ARR_SIZE)]
# print(numbers)
# v3
# numbers = [i for i in range(ARR_SIZE) if i % 2 == 0]
# print(numbers)

# negative_numbers_sum = 0
# even_numbers_sum = 0
# odd_numbers_sum = 0
# result_sum = 0
# for number in numbers:
#     if number < 0:  # ■ Суму негативних чисел;
#         negative_numbers_sum += number
#     if number % 2 == 0:  # ■ Суму парних чисел;
#         even_numbers_sum += number
#     if number % 2 != 0:  # ■ Суму непарних чисел;
#         odd_numbers_sum += number
#     if number % 3 == 0:  # ■ Добуток елементів з кратними індексами 3;
#         result_sum += number
#
# print(negative_numbers_sum)
# print(even_numbers_sum)
# print(odd_numbers_sum)
# print(result_sum)

# ■ Добуток елементів між мінімальним та максимальним елементом;
# min_value_index = numbers.index(min(numbers))
# max_value_index = numbers.index(max(numbers))
#
# if min_value_index > max_value_index:
#     min_value_index, max_value_index = max_value_index, min_value_index
#
# result = 0
# for i in range(min_value_index + 1, max_value_index):
#     result += numbers[i]
#
# print(result)

# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
# first_positive_index = last_positive_index = 0
# for i in range(ARR_SIZE):
#     if numbers[i] > 0:
#         first_positive_index = i
#         break
#
# for i in range(ARR_SIZE - 1, -1, -1):
#     if numbers[i] > 0:
#         last_positive_index = i
#         break
#
# print(first_positive_index, last_positive_index)
#
# result = 0
# for i in range(first_positive_index + 1, last_positive_index):
#     result += numbers[i]
#
# print(result)

###################################################################################
# Кортеж (tuple) – константний (immutable) список
# можна працювати як зі звичайним списком,
# тільки не можна нічого міняти (функції, які змінюють колекцію - відсутні в кортежі)
# crud -> create, read, update, delete (у кортежі можна робити лише read)

# info = ("test1", 123)
# print(info)
# print(type(info))
#
# info = "test2", 1234, 123445
# print(info)
# print(type(info))
# #
# print(info[0])
#
# info[0] = 123  # TypeError: 'tuple' object does not support item assignment

# num = int(input("Enter number: "))
# nums = 12, int(input("Enter number: ")), num
# print(nums)

#####
# import copy
#
# info = "test2", 1234, 123445
# test = copy.deepcopy(info)
# print(test)
#
# info_copy = info
# print(info_copy)
# print(info)
#
# info_list = list(info)
# print(info_list)
# info_list.append(123)
# print(info_list)
# print(info)
# info = tuple(info_list)
# print(info)
# print(info_list)
# print(info[1:3])
# print(info)

###########
# for num in 1, 3, 4, 5, 6, "Hello", 7:
#     print(num)
#
# for i in range(5):  # 0, 1, 2, 3, 4
#     print(i)
#
# for _ in range(5):
#     print("Hello")

# таку змінну створювати не можна так як оскільки її складно читати та зрозуміти
# _ = "Vasya"
# print(_)

# print(range(5))
# print(range(1, 5))
# print(range(1, 5, 2))
# result = range(5)
# print(result)
# print(type(result))
#
# numbers = list(range(10))
# print(numbers)
#
# numbers = list(range(3, 10))
# print(numbers)
#
# numbers = list(range(1, 10, 2))
# print(numbers)
#
# numbers = list(range(10, 0, -1))
# print(numbers)
#
# numbers = tuple(range(10, 0, -1))
# print(numbers)
#
# result = sorted(numbers)
# print(result)
# print(numbers)

#############
##
# dict -> словник, колекція key: value

# users = {
#     1: "John",
#     2: "Vasya",
#     3: "Petya",
#     "key1": "some-value",
#     2.4: 123,
#     True: 111,
#     2: "qwerty",  # дублювати ключі не можна!
# }
#
# print(users)
# print(type(users))
# print(users[1])  # [1] -> це не індекс, а key
# print(users["key1"])
# print(users[2.4])
# print(users[True])
# print(users[2])
#
# users_list = [
#     ("+111123455", None),
#     ("+384767557", "Bob"),
#     ("+958758767", "Alice")
# ]
#
# users_dict = dict(users_list)
# print(users_dict)
#
# users_list = list(users_dict)
# print(users_list)

###########
##
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }

# print(users["+33333333"])
# users["+33333333"] = "Petya"
# print(users["+33333333"])
#
# users["+4444444"] = "Test"
# print(users["+4444444"])
#
# print(users)
#
# for key in users:
#     print(users[key], end=" ")
#
# print()
# #
# for key in users.keys():
#     print(key, end=" ")
#
# print()
# print(users.keys())
# print(list(users.keys()))
# #
# for value in users.values():
#     print(value, end=" ")
#
# print()
# print(users.values())
#
# print()
# for key, value in users.items():
#     print(f"key: {key} value: {value}")
#
# print()
# print(users.items())

#####
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
#
# # print(users["+33333333"])
# print(users.get("+33333333", "key not exists"))
#
# # del users["+55555555"]
# deleted_value = users.pop("+555555551", "key not exists")
# print(deleted_value)
# print(users)
#
# users.clear()
# print(users)

##
# users_1 = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
# #
# users_copy = users_1.copy()
#
# print(users_1)
# print(users_copy)
# users_copy[111] = "qqqqqq"
# print(users_1)
# print(users_copy)
#
# users_2 = {
#     "+11111111": "eeeeeee",
#     "+44444": "qqqqqq",
#     "+12341234": "wwwwwww"
# }
# #
# users_1.update(users_2)
# print(users_1)
# print(users_2)

################
# json
# users = {
#     "Vasya": {
#         "phone": "123123",
#         "email": "qwerty1@gmail.com",
#         "hobbies": ["one", "two", "three"]
#     },
#     "Petya": {
#         "phone": "1345555",
#         "email": "aqwfafdbsdb@gmail.com",
#         "hobby": "uerhukjshbdjbkhdf",
#         "add_data": {
#             1: "test-1",
#             2: "test-2",
#         }
#     }
# }

# print(users["Vasya"]["hobbies"][1])
# print(users["Petya"]["add_data"][2])

##
# v1
# key = input("Enter key: ")
# if key in users:
#     print(users[key])
# else:
#     print("Nothing found!")

# v2
# key = input("Enter key: ").strip().lower()
# for curr_key in users.keys():
#     if curr_key.lower() == key:
#         print(users[curr_key])
#         break
# else:
#     print("Nothing found!")

##############
# # Множини (set) представляють ще один вид набору, який зберігає тільки унікальні елементи.
# Дублікати значень буде видалено.
# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
# print(type(users))
# #
# people = ["Mike", "Bill", "Ted"]
# users = set(people)
# print(users)
# # # #
# print(len(users))
# # #
# users.add("Sam")
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
# #
# user = "Tom"
# if user in users:
#     users.remove(user)  # якщо немає значення – генерується виняток
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
# #
# users.discard("Tim")  # елемент "Tim" відсутній, і метод нічого не робить
# print(users)
# # #
# users.clear()
# print(users)
# #
# users = {"Tom", "Bob", "Alice"}
#
# for user in users:
#     print(user)
#
# # copy() копіювання працює так само як і в list, dict і тд
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.union(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Tom", "Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.intersection(users2)  # перетин множин (що загальне у першої множини з другим)
# # v2
# print(users & users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
# users.intersection_update(users2)  # те саме, тільки результат буде записаний в users
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.difference(users2)  # що є тільки першим і немає у другій множині
# print(users3)  # {"Tom", "Alice"}
# # v2
# print(users - users2)
# #
# users.difference_update(users2)
# print(users)
# print(users2)
# #
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# # v1
# users3 = users.symmetric_difference(users2)  # унікальні значення першої та другої множин
# print(users3)
# # v2
# users4 = users ^ users2
#
# ##
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issubset(superusers))  # True
# print(superusers.issubset(users))  # False
#
#
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issuperset(superusers))  # False
# print(superusers.issuperset(users))  # True
#
#
# # Тип frozen set є видом множин, які не можуть бути змінені (за типом tuple у list)
# users = frozenset({"Tom", "Bob", "Alice"})
# print(users)
# users = set(users)
# print(users)
# # можна використовувати всі функції звичайного set, крім тих, що модифікують значення
#
####################################################################################################################################################################   28.01.2024
# # створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
# import random
#
# numbers = []
#
# for i in range(5):
#     numbers.append([])
#     for j in range(5):
#         numbers[i].append(random.randint(10, 99))
#
# for i in range(5):
#     for j in range(5):
#         print(numbers[i][j], end=" ")
#     print()
#
# # - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# # (аналогічно зробити з рядком)
#
# first_col = 2
# second_col = 4
#
# if 0 < first_col <= 5 and 0 < second_col <= 5:
#     for i in range(5):
#         numbers[i][first_col - 1], numbers[i][second_col - 1] = numbers[i][second_col - 1], numbers[i][first_col - 1]
# else:
#     print("Invalid columns!")
#
# print()
# for i in range(5):
#     for j in range(5):
#         print(numbers[i][j], end=" ")
#     print()
#
# print()
# first_row = 2
# second_row = 4
#
# if 0 < first_row <= 5 and 0 < second_row <= 5:
#     numbers[first_row - 1], numbers[second_row - 1] = numbers[second_row - 1], numbers[first_row - 1]
#     # print(numbers[first_row - 1])
#     # print(numbers[second_row - 1])
# else:
#     print("Invalid rows!")
#
# for i in range(5):
#     for j in range(5):
#         print(numbers[i][j], end=" ")
#     print()
#
# print()

#############
# def say_hello():
#     print("Hello")
#
#
# try:
#     number = 10
#     print(number)
#     print(say_hello)
#     say_hello()  # виклик функції (функція починає працювати)
#     say_hello()
# except Exception:
#     print("Something went wrong")
#
#
# def say_hello():
#     print("Hello Friends!")
#
#
# say_hello()
#
#
# def say_hello(name):
#     print(f"Hello {name}!")
#     name = "qqqq"
#     print(f"Hello {name}!")
#
#
# say_hello("Test user")
# name = "Anton"
# say_hello(name)
# print(name)

# def say_hello_name(username):
#     print(f"Hello, {username}")
#
#
# say_hello_name("Vasya")
# name = "Petya"
# say_hello_name(name)
#
# number: int = 10
# print(number)

# def user_info(name: str, age: int, hobby: str) -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# try:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     user_hobby = input("Enter your hobby: ")
#     user_info(name, age, user_hobby)
# except Exception as e:
#     print(e)

########
# після того як відпрацює ключове слово return - функція припиняє свою роботу (тільки функція)
# return – поверне результат роботи функції. Після відпрацьовування return - решта дій функції не відпрацюють
# та функція завершить свою роботу. Якщо у функції є цикл - у циклi return працює як break,
# але на відміну від break – поверне результат, а не просто
# Зупинить дії. Якщо функції є цикли, і в одному з циклів спрацював return - функція припинить свою роботу.
# ключове слово return може зустрічатися в тілі функції скільки завгодно разів

# if isinstance(n1, int) or isinstance(n1, float):
# def add(n1, n2):
#     return n1 + n2
#
#
# def sub(n1, n2):
#     return n1 - n2
#
#
# def mult(n1, n2):
#     return n1 * n2
#
#
# def division(n1, n2):
#     return n1 / n2
#
#
# def calculate() -> None:
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
#     math_operation = input("Enter math operation + - * / ")
#
#     match math_operation:
#         case "+":
#             print(f"{first_number} {math_operation} {second_number} = {add(first_number, second_number)}")
#         case "-":
#             print(f"{first_number} {math_operation} {second_number} = {sub(first_number, second_number)}")
#         case "*":
#             print(f"{first_number} {math_operation} {second_number} = {mult(first_number, second_number)}")
#         case "/":
#             print(f"{first_number} {math_operation} {second_number} = {division(first_number, second_number)}")
#         case _:
#             raise Exception("Invalid math operation!")
#
#
# try:
#     calculate()
# except ZeroDivisionError:
#     print("Do not divide by zero please!")
# except Exception as error:
#     print(error)

###
# def test():
#     return 10
#
#
# print(test())
#
#
# def test():
#     print("hello")
#
#
# print(test())
###

# def user_info(name: str, age: int = 18, hobby: str = "no hobby") -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# # user_info("Vasya", 33, "test")
# # user_info("Vasya", 33)
# # user_info("Vasya")
#
# # user_info("walking", "Petya", 33)
# user_info(hobby="walking", name="Petya", age=33)

#####
## Усі параметри,
# які розташовуються праворуч від символу *, отримують значення лише на ім'я:

# def print_person(name, *, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Bob", age=41, company="Microsoft")
#
#
# def print_person(*, name, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person(name="Bob", age=41, company="Microsoft")

# Якщо навпаки треба визначити параметри, яким можна передавати значення лише за позицією,
# тобто позиційні параметри, можна використовувати символ /: всі параметри, які йдуть до символу / ,
# є позиційними і можуть отримувати значення лише за позицією

# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Tom", company="JetBrains", age=24)  # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)

#
# def print_person(name, /, age=18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Sam", company="Google")  # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company="Microsoft", age=42)  # Name: Bob  Age: 42  company: Microsoft

####
# import random
# import string
#
# PASSWORD_DATA = string.ascii_letters + string.digits + string.punctuation
# MIN_PASSWORD_LENGTH = 16
# MAX_PASSWORD_LENGTH = 32
#
#
# def generate_password(password_length: int, initial_password_data: str) -> str:
#     if password_length < MIN_PASSWORD_LENGTH or password_length > MAX_PASSWORD_LENGTH:
#         raise Exception(f"Provided password length must be between {MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH}")
#     password = ""
#     for _ in range(password_length):
#         password += random.choice(initial_password_data)
#
#     return password
#
#
# try:
#     new_password = generate_password(1, PASSWORD_DATA)
#     print(f"New password: {new_password}")
# except Exception as error:
#     print(error)

###############
# import random
#
# words = ["Cat", "Apple", "Dog", "Letter", "Helicopter"]
#
# secret_word = random.choice(words)
# # print(secret_word)
#
# # print("_" * len(secret_word))
# user_word = ["_"] * len(secret_word)
#
# attempts_counter = 0
#
# while True:
#     # v1
#     if "".join(user_word).find("_") == -1:
#         print(f"\nYou guessed the word {secret_word}!\nAttempts: {attempts_counter}")
#         break
#     # v2
#     # if "".join(user_word).lower() == secret_word.lower():
#     #     print(f"\nYou guessed the word {secret_word}!\nAttempts: {attempts_counter}")
#     #     break
#
#     print(" ".join(user_word))
#
#     letter = input("Enter a letter: ").strip().lower()
#
#     if not letter.isalpha() or len(letter) != 1:
#         print("Please enter only one letter!")
#         continue
#
#     attempts_counter += 1
#
#     for i in range(len(secret_word)):
#         if letter == secret_word[i].lower():
#             user_word[i] = letter

# добавить ограничение на кол-во попыток, если не уложились в кол-во - проиграли

# добавить:
# - два уровня сложности
# легкий уровень: кол-во попыток равно длина слова * 2 -> если не угадал - вывести сообщение об этом
# сложный уровень: кол-во попыток равно длина слова * 1.5 -> если не угадал - вывести сообщение об этом
# показывать сколько попыток осталось
# - обработку исключений
# #
# import random
#
# NUM_SIZE = 10
# list_num = []
#
# for i in range(NUM_SIZE):
#     list_num .append(random.randint(0, 20))
#
# print(list_num)
#
# product = list_num.mult(list_num)
# print("Добуток елементів списку:", list_num)

################ Homework 6

import random

NUM_SIZE = 5
list_num = []

for i in range(NUM_SIZE):
    list_num .append(random.randint(1, 5))

print(list_num)

################ Homework 6-1

def multiply_list_elements(list_num):

    result = 1
    for num in list_num:
        result *= num
    return result

multiply_list = multiply_list_elements(list_num)
print("Multiply list elements: ", multiply_list)

################# Homework 6-2

def find_minimum(list_num):
    if not list_num:
        return None
    min_element = list_num[0]
    for num in list_num:
        if num < min_element:
            min_element = num
    return min_element

min_value = find_minimum(list_num)
print("Minimum in list: ", min_value)

################# Homework 6-3

def is_prime(n):

    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(list_num):

    count = 0
    for num in list_num:
        if is_prime(num):
            count += 1
    return count

prime_count = count_primes(list_num)
print("The number fo prime numbers in the list: ", prime_count)

################# Homework 6-4

def remove_element(list_num, target):

    count_removed = 0
    if target not in list_num:
        print("There is no this number!")
    else:
        while target in list_num:
            list_num.remove(target)
            count_removed += 1
    return count_removed

target_number =  int(input("Enter number to remove: "))
removed_count = remove_element(list_num, target_number)
print("Removed items count: ", removed_count)
print("List after removing: ", list_num)

################# Homework 6-5

first_list = [7, 5, 3, 5, 2]
second_list = [4, 5, 6, 3]

def merge_lists(first_list, second_list):

    merged_list = first_list + second_list
    return merged_list

merged = merge_lists(first_list, second_list)
print("Merged list: ", merged)

################# Homework 6-6

def power_of_elements(list_num, power):

    powered_list = [num ** power for num in list_num]
    return powered_list

power = int(input("Enter number: "))

powered_result = power_of_elements(list_num, power)
print("Powered list: ", power, powered_result)