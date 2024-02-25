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
# lenghtAB = int(input("Enter first number: "))
# lenghtCD = int(input("Enter second number: "))
# area = ((lenghtAB * lenghtCD)/2)
# print (f"lenghtAB: {lenghtAB} lenghtCD: {lenghtCD}")
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
# smalest = n1 <= n2 and n1 <= n3
# arithmetic_mean = (n1 + n2 + n3) / 3
#
# biggest_calculating = 1
# smalest_calculating = 2
# arithmetic_mean_calculating = 3
#
# print("task #: 1 biggest_calculating, 2 smalest_calculating 3 arithmetic_mean_calculating")
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
#     if 2 == smalest_calculating:
#         if task == smalest_calculating:
#             if n1 <= n2 and n1 <= n3:
#                 print(f"smalest: {n1}")
#
#             elif n2 < n1 and n2 < n3:
#                 print(f"smalest: {n2}")
#
#             elif n3 < n1 and n3 < n3:
#                 print(f"smalest: {n3}")
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
#             print(f"meters_to_miles_mean_calculating: {m1eters_to_inches}")
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
#     print(f"ZeroDivisionError occured: {error}")
# except ValueError as error:
#     print("Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except Exception as error:
#     print(f"Exeption occurred: {error}")
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
#         pritn("Exit...")
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
#         print("contonue...")
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
#
sum_nums = 0
count = 0

try:
    while True:
        num = int(input("Enter number: "))

        if num == 0:
            print("end...")
            break

        sum_nums += num
        count += 1

    average = sum_nums / count
    print(f"sum_nums: {sum_nums}")
    print(f"count: {count}")
    print(f"average: {average}")
except ValueError as e:
    print("Enter numbers only")
except Exception as e:
    print(e)

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

start = int(input("Enter start value "))
end = int(input("Enter end value: "))

if start > end:
    start, end = end, start


if start > end:
    temp = start
    start = end
    end = temp

for number in range(start, end + 1):
    is_simple = True

    if number < 2:
        continue

    for i in range(2, number):
        if number % i == 0:
            is_simple = False
            break

    if is_simple:
        print(number, end=" ")

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
# print("hello, \"world\"\n\tfrom program")
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

# sentance = "Hello, world"
# # for letter in sentance:
# #     print(letter, end=" ")
# #
# # print()
#
# for i in range(len(sentance)):
#     print(sentance[i], end=" ")
#
# # ###############################
#
# sentance = "Hello worl"
# print(sentance[:])
# print(sentance[0:])
# print(sentance[2:])
# print(sentance[2:8])
# print(sentance[1:10:2])
# print(sentance[::-1])
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