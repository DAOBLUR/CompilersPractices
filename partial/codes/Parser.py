import csv
from NodeStack import NodeStack


def CreateTable(file):
  with open(file, newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    table = [row for row in rows]
  return table


def ReplaceStack(node, token, parseTable):
  if node.symbol in parseTable.NotTerminals:
    stack = []
    indexLex = parseTable.Headers.index(token.lexeme)
    indexSym = parseTable.NotTerminals.index(node.symbol)
    text = parseTable.Table[indexSym + 1][indexLex + 1]
    text = text.split()
    for i in text:
      if i in parseTable.NotTerminals: stack.append(NodeStack(i, False))
      else: stack.append(NodeStack(i, True))
    return stack
  else:
    return [node]


def PrintStack(Stack):
  if (len(Stack) < 1):
    print('Stack: ')
    return
  symbols = Stack[0].symbol
  for i in range(1, len(Stack)):
    symbols += ' ' + Stack[i].symbol
  print('Stack: ', symbols)


def TreeGenerator(node, Stack):
  if (len(Stack) < 1 or node.id == 2): return ''

  code = f'{node.id} [ label="{node.symbol}" ];\n'
  for i in range(0, len(Stack)):
    if (node.id != Stack[i].id):
      code += f'{Stack[i].id} [ label="{Stack[i].symbol}" ];\n'
      code += f'{node.id} -> {Stack[i].id};\n'
  return code


def PrintTokens(Tokens):
  symbols = Tokens[0].symbol
  for i in range(1, len(Tokens)):
    symbols += ' ' + str(Tokens[i].symbol)
  print('Tokens: ', symbols)


def Error(Stack, Tokens):
  if (len(Stack) > 1):
    return 'Expected: ' + f'{Stack[0].symbol} in [{Tokens[0].line},{Tokens[0].pos-1}]'
  else:
    return 'Not expected: ' + f'{Tokens[0].lexeme} : "{Tokens[0].symbol}" in [{Tokens[0].line},{Tokens[0].pos}]'


def Parser(stack, tokens, parseTable):
  #PrintStack(stack)
  #PrintTokens(tokens)
  tree = 'digraph G {\n'
  i = 1
  while True:
    if stack[0].symbol == '$' and tokens[0].lexeme == '$':
      tree += '}'
      return True, tree

    if stack[0].symbol == tokens[0].lexeme and stack[0].terminal == True:
      pop = (stack.pop(0)).symbol
      pop += ' ' + (tokens.pop(0)).lexeme

    if stack[0].symbol == 'ε':
      pop = (stack.pop(0)).symbol

    if stack[0].symbol != tokens[0].lexeme and stack[0].terminal == True:
      return False, Error(stack, tokens)
    node = stack.pop(0)

    replace = ReplaceStack(node, tokens[0], parseTable)

    tree += TreeGenerator(node, replace)
    stack = replace + stack
    i += 1

  #PrintStack(stack)
  #PrintTokens(tokens)
