import string
user_input = input()
for char in string.punctuation:
    user_input = user_input.replace(char, '')
print("#" + user_input.title().replace(" ","")[:140])