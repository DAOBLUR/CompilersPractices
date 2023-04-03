import ply.lex as lex

reserved = {
  'main' : 'main',
  'var'  : 'var',
  'null' : 'null',
  'return': 'return',
  'func': 'funcion',
  'print' : 'print',
  'read' : 'read',
  'if' : 'if',
  'elif' : 'elseif',
  'else' : 'else',
  'for' : 'for',
  'while' : 'while'
}

# List of token names. This is always required
tokens = ['FLOAT', 'INT','STRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN','LKEY', 'RKEY', 'EQUAL', 'GREATER',
  'LESS', 'EQUALEQUAL', 'LESSEQUAL', 'GREATEREQUAL', 'DIFERENT', 'COMMENT', 'COMMENTOPEN', 'COMMENTCLOSE', 'IDENTIFIER', 'COMMA', 'OR', 'AND' ] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_LKEY = r'{'
t_RKEY = r'}'
t_EQUAL = r'='
t_GREATER = r'>'
t_LESS = r'<'
t_EQUALEQUAL = r'=='
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_DIFERENT = r'!='
t_COMMENT = r'//.*'
t_COMMENTOPEN = r'/\*'
#t_COMMENTOPEN = r'/\*(\n| |.)*'
t_COMMENTCLOSE = r'\*/'
t_COMMA = r','
t_OR = r'\|'
t_AND = r'&'


# A regular expression rule with some action code
def t_FLOAT(t):
  r'\d+\.\d+'
  t.value = float(t.value) 
  t.type = reserved.get(t.value,'FLOAT') 
  return t

def t_INT(t):
  r'\d+'
  t.value = int(t.value) 
  t.type = reserved.get(t.value,'INT') # 
  return t

def t_STRING(t):
  r"(\"|\') (\n|\t||.|(\d)|\n|)*(\"|\')"
  t.type = reserved.get(t.value,'STRING') # 
  return t

  
# A regular expression rule with some action code
def t_IDENTIFIER(t):
  r'[a-zA-Z]([a-zA-Z]|(\d+)|(_))*'

  t.type = reserved.get(t.value,'IDENTIFIER') # guardamos el valor del lexema
  return t
  
# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
  
# A string containing ignored characters (spaces and tabs)
t_ignore = '\t\n '
  
# Error handling rule
def t_error(t):
  print("Illegal character ’ %s’" % t.value[0])
  t.lexer.skip(1)
  
# Build the lexer
lexer = lex.lex()

# Test it out
data = ""

with open('example2.ds', 'r') as file: data = file.read()
# Give the lexer some input
lexer.input(data)

# Tokenize
out = open("out2.txt", "w")
while True:
  tok = lexer.token()
  if not tok: break 
  print(tok)
  out.write(str(tok)+"\n")
out.close()