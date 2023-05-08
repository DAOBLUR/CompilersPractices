class ParseTable:

  def __init__(self, table):
    self.Table = table
    self.NotTerminals = []
    i = 1
    while i < len(table):
      self.NotTerminals.append(table[i][0])
      i += 1

    self.Headers = []
    i = 1
    while i < len(table[0]):
      self.Headers.append(table[0][i])
      i += 1

  def Print(self):
    print('')
    for i in self.Table:
      print(i)
    print('')