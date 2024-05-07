# get two numbers from user
# get operation from user
# perform operation on numbers
# print result to terminal
import json

with open(
    "calculator_messages.json", "r") as file:
    data = json.load(file)
messages = data

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def invalid_language(language_c):
    if language_c not in ['english', 'japanese', '日本語']:
        return True
    return False

def validate_number(number):
    while invalid_number(number):
        prompt(messages['invalid'])
        number= input()

def return_result(operation):
    while operation not in ["1", "2", "3", "4"]:
        prompt(messages['choose'])
        operation = input()
    match operation:
        case '1':
            return (float(num1) + int(num2))
        case '2':
            return (float(num1) - int(num2))
        case '3':
            return (float(num1) * float(num2))
        case '4':
            try:
                output = float(num1) // float(num2)
            except ZeroDivisionError:
                return messages['zero']
            return output

def select_language(language):
    while invalid_language(language.lower()):
        prompt("invalid language")
        language = input()
    match language:
        case 'english':
            message_language = data.get('english')
        case 'japanese':
            message_language = data.get('japanese')
        case '日本語':
            message_language = data.get('japanese')
    return message_language

prompt("Select a language: English or 日本語")
messages = (select_language(input()))
prompt(messages['start'])
while True:

    prompt(messages['first'])
    num1 = input()
    validate_number(num1)

    prompt(messages['second'])
    num2 = input()
    validate_number(num2)

    prompt(f"{num1} {num2}")
    prompt(messages['operate'])
    result = return_result(input())

    prompt(messages['result'] + str(result))
    prompt(messages['again'])
    if input().lower() != 'y':
        break