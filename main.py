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
#
# # v1
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