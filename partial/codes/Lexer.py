import ply.lex as lex
from Token import Token

reserved = {
  'main': 'main',
  'exec': 'exec',
  'var': 'var',
  'null': 'null',
  'return': 'return',
  'func': 'func',
  'print': 'print',
  'read': 'read',
  'if': 'if',
  'elif': 'elif',
  'else': 'else',
  'for': 'for',
  'while': 'while'
}

tokens = list(reserved.values()) + [
  'float', 'int', 'string', 'plus', 'minus', 'times', 'divide', 'lparen',
  'rparen', 'lkey', 'rkey', 'equal', 'greater', 'less', 'equalequal',
  'lessequal', 'greaterequal', 'diferent', 'comment', 'multicomment', 'id',
  'comma', 'or', 'and'
]

t_plus = r'\+'
t_minus = r'-'
t_times = r'\*'
t_divide = r'/'
#
t_lparen = r'\('
t_rparen = r'\)'
t_lkey = r'{'
t_rkey = r'}'
#
t_equal = r'='
t_greater = r'>'
t_less = r'<'
t_equalequal = r'=='
t_lessequal = r'<='
t_greaterequal = r'>='
t_diferent = r'!='
#
t_comment = r'//.*'
t_multicomment = r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'
#
t_comma = r','
#
t_or = r'\|'
t_and = r'&'


def t_float(t):
  r'\d+\.\d+'
  t.value = float(t.value)
  t.type = reserved.get(t.value, 'float')
  return t


def t_int(t):
  r'\d+'
  t.value = int(t.value)
  t.type = reserved.get(t.value, 'int')  #
  return t


def t_string(t):
  r"(\"|\') (\n|\t||.|(\d)|\n|)*(\"|\')"
  t.type = reserved.get(t.value, 'string')  #
  return t


def t_id(t):
  r'[a-zA-Z]([a-zA-Z]|(\d+)|(_))*'
  t.type = reserved.get(t.value, 'id')
  return t


t_ignore = '\t\n '


def t_error(t):
  print("Illegal character ’ %s’" % t.value[0])
  t.lexer.skip(1)


def GenerateTokens(path, fileName):
  outPath = 'examples/out/'
  lexer = lex.lex()
  code = ''
  tokens = []
  final = 0

  with open(path + fileName + '.ds', 'r') as file:
    code = file.read()
  lexer.input(code)

  out = open(outPath + fileName + '.out', "w")
  while True:
    myToken = lexer.token()
    if not myToken: break

    final = myToken.lineno + 1

    tokens.append(
      Token(myToken.type, myToken.type, myToken.lineno, myToken.lexpos,
            str(myToken.value)))

    out.write(str(myToken) + "\n")
  out.close()

  tokens.append(Token("$", "$", final, 1))
  return tokens
