# try:
#     print("1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n6. Saturday\n7 Sunday")
#     user_select = int(input("Enter day of the week number: "))
#
#     if user_select == 1:
#         print("Monday")
#     elif user_select == 2:
#         print("Tuesday")
#     elif user_select == 3:
#         print("Wednesday")
#     elif user_select == 4:
#         pritn("Thursday")
#     elif user_select == 5:
#         pritn("Friday")
#     elif user_select == 6:
#         pritn("Saturday")
#     elif user_select == 7:
#         pritn("Sunday")
#     else:
#         print("Incorrect day number!")
#
# except Exception as e:
#     print(f"Error: {e}")

#############################################

# try:
#     number = int(input("Enter two numbers: "))
#
#     n1 = number // 10
#     n2 = number // 1 % 10
#
#     if n1 == n2:
#         print("True")
#     if n1 > n2:
#         print(f"n2 smaler: {n2}, {n1}")
#     if n1 < n2:
#         print(f"n1 smaler: {n1}, {n2}")
#
# except Exception as e:
#     print(f"Error: {e}")

###################################################


try:
    number = int(input("Enter two numbers: "))

    n1 = number // 10
    n2 = number // 1 % 10

    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    user_select = int(input("Mathematical operation: "))

    if user_select == 1:
        addition_result = n1 + n2
        print(f"Result: {addition_result} ")
    elif user_select == 2:
        subtraction_result = n1 - n2
        print(f"Result: {subtraction_result} ")
    elif user_select == 3:
        multiplication_result = n1 * n2
        print(f"Result: {multiplication_result} ")
    elif user_select == 4:
        division_result = n1 / n2
        print(f"Result: {division_result} ")
    else:
        print("Enter correct mathematical operation number!")

except Exception as e:
    print(f"Error: {e}")