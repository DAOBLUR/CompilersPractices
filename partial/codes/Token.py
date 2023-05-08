class Token:

  def __init__(self, type, lexeme, line, pos, symbol=''):
    self.type = type
    self.lexeme = lexeme
    self.line = line
    self.pos = pos
    self.symbol = symbol