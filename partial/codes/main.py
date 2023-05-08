from Lexer import GenerateTokens
import Parser
import graphviz
import ParseTable


def main():
  path = 'examples/ds/'
  dotPath = 'examples/dot/'
  pngPath = 'examples/png/'

  fileNames = [
    'example', 'example2', 'example3', 
    'bexample', 'bexample2', 'bexample3'
  ]

  for i in fileNames:
    tokens = GenerateTokens(path, i)

    node_E = Parser.NodeStack("Program", False)
    node_dolar = Parser.NodeStack("$", True)
    stack = [node_E, node_dolar]

    table = Parser.CreateTable("table.csv")

    parseTable = ParseTable.ParseTable(table)

    message, result = Parser.Parser(stack.copy(), tokens.copy(), parseTable)

    if message:
      out = open(dotPath + i + '.dot', "w")
      out.write(result)
      out.close()

      graphviz.Source(result).render(pngPath + i, format='png', cleanup=True)
    else:
      print(f'Error in {i}.ds file: \n', result, '\n')


if __name__ == "__main__":
  main()
