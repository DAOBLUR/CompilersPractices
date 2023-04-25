import csv

counter = 1

class ParseTable:
  def __init__(self, table):
    self.Table = table
    self.NotTerminals = []
    i = 1
    while i < len(table):
      self.NotTerminals.append(table[i][0])
      i+=1
      
    self.Headers = []
    i = 1
    while i < len(table[0]):
      self.Headers.append(table[0][i])
      i+=1
      
  def Print(self):
    print('')
    for i in self.Table:
      print(i)
    print('')
    
class NodeStack:
  def __init__(self, symbol, terminal):
    global counter
    self.id = counter
    self.symbol = symbol
    self.terminal = terminal
    counter += 1

class Token:
  def __init__(self, type, lexeme, line):
    self.type = type
    self.lexeme = lexeme
    self.line = line

def CreateTable(file):
  with open(file, newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    table = [row for row in rows]
  return table

def ReplaceStack(node,token,parseTable):
  if node.symbol in parseTable.NotTerminals:
    stack = []
    indexLex = parseTable.Headers.index(token.lexeme)
    indexSym = parseTable.NotTerminals.index(node.symbol)

    print('indexLex: ',indexLex)
    print('indexSym: ',indexSym)

    print('token.lexeme: ',token.lexeme)
    print('node.symbol: ',node.symbol)
  
    text = parseTable.Table[indexSym+1][indexLex+1]
    
    print('text: ',text)
    text = text.split() 
    print('text: ',text)
    for i in text:
      if i in parseTable.NotTerminals: stack.append(NodeStack(i, False))
      else: stack.append(NodeStack(i, True))
        
    return stack
  else: return [node]

def PrintStack(Stack):
  symbols = Stack[0].symbol
  for i in range(1,len(Stack)):
    #symbols += ', ' + Stack[i].symbol
    symbols += Stack[i].symbol
  print('Stack: ',symbols)

def PrintTokens(Tokens):
  #symbols = '[' + Tokens[0].type + ',' + Tokens[0].lexeme + ']'
  symbols = Tokens[0].lexeme
  for i in range(1,len(Tokens)):
    symbols += Tokens[i].lexeme
  print('Tokens: ',symbols)

def Parser(stack,tokens,parseTable):
  print('')
  #parseTable.Print()
  PrintStack(stack)
  PrintTokens(tokens)
  i = 1
  while True:
    #print('\n','-- ',i,' --','\n')
    if stack[0].symbol == '$' and tokens[0].lexeme == '$':
      print(True)
      break
    if stack[0].symbol == tokens[0].lexeme and stack[0].terminal == True:
      pop = (stack.pop(0)).symbol
      pop += ' ' + (tokens.pop(0)).lexeme
      #print('                  terminal: ',pop)
    if stack[0].symbol == 'ε':
      pop = (stack.pop(0)).symbol
      #print('                  ε: ',pop)
    if stack[0].symbol != tokens[0].lexeme and stack[0].terminal == True:
      print(False)
      break
    node = stack.pop(0)  
    
    #print('node.symbol: ',node.symbol)
    stack = ReplaceStack(node,tokens[0],parseTable) + stack
    
    #PrintStack(stack)
    #PrintTokens(tokens)
    i+=1

#---------------------------
t1 = Token("lparen", "(", 1)
t2 = Token("int", "int", 1)
t3 = Token("operator", "+", 1)
t4 = Token("int", "int", 1)
t5 = Token("rparen", ")", 1)
t6 = Token("operator", "*", 1)
t7 = Token("int", "int", 1)
te = Token("$", "$", 1)

tokens = [t2,t6,t4,te]
tokens2 = [t1,t2,t3,t4,t5,te]
tokens3 = [t1,t2,t3,t4,t5,t6,t7,te]

node_E = NodeStack("E", False)
node_dolar = NodeStack("$", True)
stack = [ node_E, node_dolar ]

table = CreateTable("table.csv")
parseTable = ParseTable(table)

Parser(stack.copy(),tokens.copy(),parseTable)
Parser(stack.copy(),tokens2.copy(),parseTable)
Parser(stack.copy(),tokens3.copy(),parseTable)



# https://replit.com/@PrivateReplit/6ParserBottonUp#main.py