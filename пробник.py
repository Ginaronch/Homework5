import string
user_input = input()
for char in string.punctuation:
    user_input = user_input.replace(char, '')
    if len(user_input) > 140:
        user_input = user_input[:140]
print(user_input)