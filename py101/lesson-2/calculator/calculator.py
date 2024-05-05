# get two numbers from user
# get operation from user
# perform operation on numbers
# print result to terminal
# "/home/elbenoss/launch-school/py101/lesson-2/calculator/calculator_messages.json"
import json

with open(
    "calculator_messages.json", "r") as file:
    data = json.load(file)
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

while True:
    # ask for language
    prompt("Select a language: English or 日本語")
    language = input()
    while invalid_language(language.lower()):
        prompt("invalid language")
        language = input()

    match language:
        case 'english':
            messages = data.get('english')
        case 'japanese':
            messages = data.get('japanese')
        case '日本語':
            messages = data.get('japanese')

    prompt(messages['start'])

    # ask for first number
    prompt(messages['first'])
    num1 = input()
    while invalid_number(num1):
        prompt(messages['invalid'])
        num1 = input()

    #ask for second number
    prompt(messages['second'])
    num2 = input()
    while invalid_number(num2):
        prompt(messages['invalid'])
        num2 = input()

    prompt(f"{num1} {num2}")

    prompt(messages['operate'])
    operation = input()
    while operation not in ["1", "2", "3", "4"]:
        prompt(messages['choose'])
        operation = input()
    match operation:
        case '1':
            output = (float(num1) + int(num2))
        case '2':
            output = (float(num1) - int(num2))
        case '3':
            output = (float(num1) * float(num2))
        case '4':
            output = (float(num1) // float(num2))

    prompt(messages['result'] + str(output))
    prompt(messages['again'])
    if input().lower() == 'n':
        break