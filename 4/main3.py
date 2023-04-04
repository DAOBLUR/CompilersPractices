import re

def Automata(A, initialState, finalState, input):
  state = initialState
  keys = list(A.keys())
  i = 0 
  while i < len(input):
    j = GetKey(keys,state,input[i])
    if j == 0: return False
    state = A[state, keys[j-1][1]]
    i += 1
    
  if state == finalState: return True 
  return False 

def GetKey(keys,state,input):
  i = 0
  for key in keys:
    if key[0] == state and re.search(key[1],input): return i+1
    i+=1
  return 0

A = {
  ('start', r'[a-zA-Z]'): 'in_id',
  ('in_id', r'\d'): 'in_id',
  ('in_id', r'[a-zA-Z]'): 'in_id'
}


initialState = 'start'
finalState = 'in_id'

inputString = 'abcde'
result = Automata(A, initialState, finalState, inputString)
print(inputString, result)

inputString = 'a1b2c3d4e5'
result = Automata(A, initialState, finalState, inputString)
print(inputString, result)

inputString = '1a2b3c4d5e6'
result = Automata(A, initialState, finalState, inputString)
print(inputString, result)

inputString = '123456789'
result = Automata(A, initialState, finalState, inputString)
print(inputString, result)