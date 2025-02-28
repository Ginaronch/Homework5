import string
user_input = input()
if user_input.count("_") > 1 and user_input.startswith("_") and user_input.endswith("_") and len(user_input) >= 1:
    print(False)
else:
    print(True)