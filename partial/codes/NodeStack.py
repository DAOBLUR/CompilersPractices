counter = 1


class NodeStack:

  def __init__(self, symbol, terminal):
    global counter

    if symbol == '$': self.id = 2
    else: self.id = counter

    self.symbol = symbol
    self.terminal = terminal
    counter += 1
