import re

def Automata(A, initialState, finalState, input):
  matchs = []
  state = initialState
  keys = list(A.keys())
  i = 0
  j = 0
  k = 0
  l = 1
  string = ''
  
  while i < len(input):
    if input[i] == '\n': l += 1
    j = GetKey(keys, state, input[i])
    
    if j == 0:
      if string != '':
        matchs.append([string, [k, i - 1,l]])
        string = ''
      k = i + 1
      state = initialState
    else:
      state = A[state, keys[j - 1][1]]
      string += input[i]
    
    i += 1
    
  if state == finalState and string != '':
    matchs.append([string, [k, i - 1,l]])
  return matchs


def GetKey(keys, state, input):
  i = 0
  for key in keys:
    if key[0] == state and re.search(key[1], input): return i + 1
    i += 1
  return 0


A = {
  ('start', r'[a-zA-Z]'): 'in_id',
  ('in_id', r'\d'): 'in_id',
  ('in_id', r'[a-zA-Z]'): 'in_id'
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