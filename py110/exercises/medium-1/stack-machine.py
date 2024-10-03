
def minilang(command: str) -> None:
    register = 0
    stack = []
    operations = {

        'ADD': lambda x, y: x + y,
        'SUB': lambda x, y: y - x,
        'MULT': lambda x, y: x * y,
        'DIV': lambda x, y: y // x,
        'REMAINDER': lambda x, y: y % x,
    }

    for op in command.split():
        if op.startswith('-'):
            register = 0 - int(op[1::])
        elif op.isdigit():
            register = int(op)
        elif op == 'PUSH':
            stack.append(register)
        elif op == 'POP':
            register = stack.pop()
        elif op == 'PRINT':
            print(register)
        elif stack and register:
            register = operations[op](stack.pop(), register)

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)
