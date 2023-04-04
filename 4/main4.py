def Automata(A, initialState, finalState, input):
  matchs = []
  state = initialState
  i = 0
  k = 0
  l = 1
  string = ''
  
  while i < len(input):
    if input[i] == '\n': l += 1
    try:
      state = A[state,input[i]]
      string += input[i]
    except KeyError:
      if string != '':
        matchs.append([string, [k, i - 1,l]])
        string = ''
      k = i + 1
      state = initialState
    i += 1
  if state == finalState and string != '':
    matchs.append([string, [k, i - 1,l]])
  return matchs

A = {
  ('start', 'a'): 'in_id',
  ('start', 'b'): 'in_id',
  ('start', 'c'): 'in_id',
  ('start', 'd'): 'in_id',
  ('start', 'e'): 'in_id',
  ('start', 'f'): 'in_id',
  ('start', 'g'): 'in_id',
  ('start', 'h'): 'in_id',
  ('start', 'i'): 'in_id',
  ('start', 'j'): 'in_id',
  ('start', 'k'): 'in_id',
  ('start', 'l'): 'in_id',
  ('start', 'm'): 'in_id',
  ('start', 'n'): 'in_id',
  ('start', 'ñ'): 'in_id',
  ('start', 'o'): 'in_id',
  ('start', 'p'): 'in_id',
  ('start', 'q'): 'in_id',
  ('start', 'r'): 'in_id',
  ('start', 's'): 'in_id',
  ('start', 't'): 'in_id',
  ('start', 'u'): 'in_id',
  ('start', 'v'): 'in_id',
  ('start', 'w'): 'in_id',
  ('start', 'x'): 'in_id',
  ('start', 'y'): 'in_id',
  ('start', 'z'): 'in_id',
  ('start', 'A'): 'in_id',
  ('start', 'B'): 'in_id',
  ('start', 'C'): 'in_id',
  ('start', 'D'): 'in_id',
  ('start', 'E'): 'in_id',
  ('start', 'F'): 'in_id',
  ('start', 'G'): 'in_id',
  ('start', 'H'): 'in_id',
  ('start', 'I'): 'in_id',
  ('start', 'J'): 'in_id',
  ('start', 'K'): 'in_id',
  ('start', 'L'): 'in_id',
  ('start', 'M'): 'in_id',
  ('start', 'N'): 'in_id',
  ('start', 'Ñ'): 'in_id',
  ('start', 'O'): 'in_id',
  ('start', 'P'): 'in_id',
  ('start', 'Q'): 'in_id',
  ('start', 'R'): 'in_id',
  ('start', 'S'): 'in_id',
  ('start', 'T'): 'in_id',
  ('start', 'U'): 'in_id',
  ('start', 'V'): 'in_id',
  ('start', 'W'): 'in_id',
  ('start', 'X'): 'in_id',
  ('start', 'Y'): 'in_id',
  ('start', 'Z'): 'in_id',
  #-----------------------
  ('in_id', '0'): 'in_id',
  ('in_id', '1'): 'in_id',
  ('in_id', '2'): 'in_id',
  ('in_id', '3'): 'in_id',
  ('in_id', '4'): 'in_id',
  ('in_id', '5'): 'in_id',
  ('in_id', '6'): 'in_id',
  ('in_id', '7'): 'in_id',
  ('in_id', '8'): 'in_id',
  ('in_id', '9'): 'in_id',
  #-----------------------
  ('in_id', 'a'): 'in_id',
  ('in_id', 'b'): 'in_id',
  ('in_id', 'c'): 'in_id',
  ('in_id', 'd'): 'in_id',
  ('in_id', 'e'): 'in_id',
  ('in_id', 'f'): 'in_id',
  ('in_id', 'g'): 'in_id',
  ('in_id', 'h'): 'in_id',
  ('in_id', 'i'): 'in_id',
  ('in_id', 'j'): 'in_id',
  ('in_id', 'k'): 'in_id',
  ('in_id', 'l'): 'in_id',
  ('in_id', 'm'): 'in_id',
  ('in_id', 'n'): 'in_id',
  ('in_id', 'ñ'): 'in_id',
  ('in_id', 'o'): 'in_id',
  ('in_id', 'p'): 'in_id',
  ('in_id', 'q'): 'in_id',
  ('in_id', 'r'): 'in_id',
  ('in_id', 's'): 'in_id',
  ('in_id', 't'): 'in_id',
  ('in_id', 'u'): 'in_id',
  ('in_id', 'v'): 'in_id',
  ('in_id', 'w'): 'in_id',
  ('in_id', 'x'): 'in_id',
  ('in_id', 'y'): 'in_id',
  ('in_id', 'z'): 'in_id',
  ('in_id', 'A'): 'in_id',
  ('in_id', 'B'): 'in_id',
  ('in_id', 'C'): 'in_id',
  ('in_id', 'D'): 'in_id',
  ('in_id', 'E'): 'in_id',
  ('in_id', 'F'): 'in_id',
  ('in_id', 'G'): 'in_id',
  ('in_id', 'H'): 'in_id',
  ('in_id', 'I'): 'in_id',
  ('in_id', 'J'): 'in_id',
  ('in_id', 'K'): 'in_id',
  ('in_id', 'L'): 'in_id',
  ('in_id', 'M'): 'in_id',
  ('in_id', 'N'): 'in_id',
  ('in_id', 'Ñ'): 'in_id',
  ('in_id', 'O'): 'in_id',
  ('in_id', 'P'): 'in_id',
  ('in_id', 'Q'): 'in_id',
  ('in_id', 'R'): 'in_id',
  ('in_id', 'S'): 'in_id',
  ('in_id', 'T'): 'in_id',
  ('in_id', 'U'): 'in_id',
  ('in_id', 'V'): 'in_id',
  ('in_id', 'W'): 'in_id',
  ('in_id', 'X'): 'in_id',
  ('in_id', 'Y'): 'in_id',
  ('in_id', 'Z'): 'in_id'
}

initialState = 'start'
finalState = 'in_id'

data = ''

with open('example.ds', 'r') as file:
  data = file.read()
tokens = Automata(A, initialState, finalState, data)

out = open("out1.txt", "w")
for token in tokens:
  print(token)
  out.write(str(token) + "\n")
out.close()

print('------------------------------------------')

with open('example2.ds', 'r') as file:
  data = file.read()
tokens = Automata(A, initialState, finalState, data)

out = open("out2.txt", "w")
for token in tokens:
  print(token)
  out.write(str(token) + "\n")
out.close()