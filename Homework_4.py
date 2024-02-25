# text = input("Enter some text: ")
#
# letter_count = 0
# digit_count = 0
#
# for symbol in text:
#    if symbol.isalpha():
#        letter_count += 1
#    elif symbol.isdigit():
#        digit_count += 1
#
# print("Number of letters:", letter_count)
# print("Number of digits:", digit_count)

##################################
#
# text = input("Enter some text: ")
# count = 0
# search = input("Enter letter you would like to find: ")
# for letter in text:
#     if letter == search:
#         count += 1
# print("result:", count)

##################################
#
# text = input("Enter the original string: ")
#
# search_word = input("Enter the word to replace: ")
# replace_word = input("Enter the replacement word: ")
# corrected_text = text.replace(search_word, replace_word)
#
# print("Corrected text: " + corrected_text)
########################################

count = 0

text = "Hello my neighbors"

print(text[2:3])
print(text[16:17])
print(text[:5])
print(text[:16])
print(text[0:18:2])
print(text[1:18:2])
print(text[::-1])
print(text[::-2])

print(len(text))

