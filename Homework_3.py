try:
    print("1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n6. Saturday\n7 Sunday")
    user_select = int(input("Enter day of the week number: "))

    if user_select == 1:
        print("Monday")
    elif user_select == 2:
        print("Tuesday")
    elif user_select == 3:
        print("Wednesday")
    elif user_select == 4:
        pritn("Thursday")
    elif user_select == 5:
        pritn("Friday")
    elif user_select == 6:
        pritn("Saturday")
    elif user_select == 7:
        pritn("Sunday")
    else:
        print("Incorrect day number!")

except Exception as e:
    print(f"Error: {e}")