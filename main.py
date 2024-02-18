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
################################################
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

