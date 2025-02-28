import keyword
import string
user_input = input()
if user_input[0].isdigit():
        print(False)
elif " " in user_input:
    print(False)
elif any(element.isupper() for element in user_input):
    print(False)
elif any(element in string.punctuation.replace("_", "") for element in user_input):
    print(False)
elif user_input.count("_") > 1 and all(char == "_" for char in user_input):
    print(False)
elif user_input in keyword.kwlist:
    print(False)
else:
    print(True)
#ne komititsa