# with match-case
weather = input('Enter weather condition (sunny, rainy, etc.): ').lower()
match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case _:
        print("Let's stay inside.")