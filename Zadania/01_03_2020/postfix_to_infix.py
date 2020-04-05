expression = '1 2 + 3 * 6 + 2 3 + /'
result = ''
character_list = expression.split()
print(expression)
print(character_list)

def postfix_to_infix(characters):
    stack = []
    for element in characters:
        if element.isdigit():
            stack.append(element)
            print(stack)
        else:
            stack[-2] = '(' + stack[-2] + element + stack[-1] + ')'
            stack.remove(stack[-1])
            print(stack)
    return stack[0]

print("Wyrażenie w postaci postfix = %s" % (expression))
result = postfix_to_infix(character_list)
print("Wyrażenie do obliczenia = %s" % (result))
print("Wynik wyrażenia = %d" % (eval(result)))
