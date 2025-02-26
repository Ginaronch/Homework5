answer = "yes"
while answer == "yes":
 print('Введите первое число: ')
 user_input1 = input()
 print('Введите второе число: ')
 user_input2 = input()
 number1 = float(user_input1)
 number2 = float(user_input2)
 sign = input("Введите знак (+, -, *, /): ")
 if sign == '+':
     print('Ответ:', number1 + number2)
 elif sign == '-':
     print('Ответ:', number1 - number2)
 elif sign == '*':
     print('Ответ:', number1 * number2)
 elif sign == '/':
     if number2 == 0:
         print('вспомни уроки математики!')
     elif number2 != 0:
         print('Ответ:', number1 / number2)
 else:
     print('Неизвестный знак!')
 answer = input('Желаете продолжить? yes/no: ')
 if answer != "yes":
     break