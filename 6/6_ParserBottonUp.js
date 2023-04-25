
let counter = 1;

class ParseTable {
  constructor(table) {
    this.Table = table;

    this.NotTerminals = [];
    let i = 1;
    while (i < table.length) {
      this.NotTerminals.push(table[i][0]);
      i++;
    }
    this.Headers = [];
    i = 1;

    while (i < table[0].length) {
      this.Headers.push(table[0][i]);
      i++;
    }
  }

  Print() {
    console.log("");
    for (let i = 0; i < this.Table.length; i++) {
      console.log(this.Table[i]);
    }
    console.log("");
  }
}

class NodeStack {
  constructor(symbol, terminal) {
    globalThis.counter;
    this.id = counter;
    this.symbol = symbol;
    this.terminal = terminal;
    counter += 1;
  }
}

class Token {
  constructor(type, lexeme, line) {
    this.type = type;
    this.lexeme = lexeme;
    this.line = line;
  }
}

const CreateTable = require('./read.js');

async function GetTable(fileName) {
    let table = [];
    try {
        table = await CreateTable(fileName);
    } 
    catch (error) {
        console.error(error);
    }
    return table;
}

function ReplaceStack(node, token, parseTable) {
    if (parseTable.NotTerminals.includes(node.symbol)) {
        const stack = [];
        const indexLex = parseTable.Headers.indexOf(token.lexeme);
        const indexSym = parseTable.NotTerminals.indexOf(node.symbol);

        console.log('indexLex: ',indexLex)
        console.log('indexSym: ',indexSym)

        console.log('token.lexeme: ',token.lexeme)
        console.log('node.symbol: ',node.symbol)

        let text = parseTable.Table[indexSym + 1][indexLex + 1];

        
        console.log('text: ',text)
        text = text.split(" ");
        console.log('text: ',text)

        for (let i = 0; i < text.length; i++) {
            if (parseTable.NotTerminals.includes(text[i])) {
                stack.push(new NodeStack(text[i], false));
            } 
            else {
                stack.push(new NodeStack(text[i], true));
            }
        }
        return stack;
    } 
    else {
        return [node];
    }
}

function PrintStack(Stack) {
    let symbols = Stack[0].symbol;
    for (let i = 1; i < Stack.length; i++) {
        symbols += Stack[i].symbol;
    }
    console.log("Stack: ", symbols);
}

function PrintTokens(Tokens) {
    let symbols = Tokens[0].lexeme;
    for (let i = 1; i < Tokens.length; i++) {
        symbols += Tokens[i].lexeme;
    }
    console.log("Tokens: ", symbols);
}

function Parser(stack, tokens, parseTable) {
    console.log();
    PrintStack(stack);
    PrintTokens(tokens);
    let i = 1;

    while (true) {
        if (stack[0].symbol === "$" && tokens[0].lexeme === "$") {
            console.log(true);
            break;
        }
        if (stack[0].symbol === tokens[0].lexeme && stack[0].terminal === true) {
            let pop = stack.shift().symbol;
            pop += " " + tokens.shift().lexeme;
        }
        if (stack[0].symbol === "ε") {
            let pop = stack.shift().symbol;
        }
        if (stack[0].symbol !== tokens[0].lexeme && stack[0].terminal === true) {
            console.log(false);
            break;
        }
        const node = stack.shift();
        stack = ReplaceStack(node, tokens[0], parseTable).concat(stack);
        i++;
    }
}

async function main() {
    try {
        let t1 = new Token("lparen", "(", 1);
        let t2 = new Token("int", "int", 1);
        let t3 = new Token("operator", "+", 1);
        let t4 = new Token("int", "int", 1);
        let t5 = new Token("rparen", ")", 1);
        let t6 = new Token("operator", "*", 1);
        let t7 = new Token("int", "int", 1);
        let te = new Token("$", "$", 1);

        let tokens = [t2,t6,t4,te];
        let tokens2 = [t1,t2,t3,t4,t5,te];
        let tokens3 = [t1,t2,t3,t4,t5,t6,t7,te];

        let node_E = new NodeStack("E", false);
        let node_dolar = new NodeStack("$", true);
        let stack = [ node_E, node_dolar ];

        var table = await GetTable('table.csv');
        //console.log('146: ',table);
        let parseTable = new ParseTable(table);

        Parser(stack.slice(),tokens,parseTable);
        Parser(stack.slice(),tokens2,parseTable);
        Parser(stack.slice(),tokens3,parseTable);

    }
    catch (error) {
        console.error(error);
    }
}
 
main();