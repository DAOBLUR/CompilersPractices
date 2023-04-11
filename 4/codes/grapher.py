from graphviz import Digraph
from IPython.display import Image

def CreateAutomata(name):
  g = Digraph()
  g.node('invisible', style='invisible')
  finalStates = []
  transitions = []
  initialStates = []

  print('1-Input Initial States: ')
  while True:
    inputState = input('initial state: ')
    if inputState == '': break
    initialStates.append(inputState)

  print('2-Input Final States: ')
  while True:
    inputState = input('final state: ')
    if inputState == '': break
    finalStates.append(inputState)

  print('3-Input Transitions: ')
  while True:
    sourceState = input('source state: ')
    destinationState = input('destination state: ')
    inputValue = input('input value: ')
    
    if sourceState =='' and destinationState == '' and inputValue == '': break
    transitions.append([sourceState, destinationState, inputValue])

  for initialState in initialStates: g.edge('invisible', initialState, dir='front', arrowhead='vee')

  for finalState in finalStates: g.node(finalState, shape='circle', peripheries='2')

  for transition in transitions: g.edge(transition[0], transition[1], label=transition[2])

  g.render(name, format='png', view=True)  



  