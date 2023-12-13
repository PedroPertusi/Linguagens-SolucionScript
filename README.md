# Linguagens-SolucionScript

Alunos: Pedro Pertusi e Lucca Hiratsuca

## Introdução

O SolucionScript é uma linguagem de programação criada pensando na lingua espanhola, com o objetivo de ser simples e intuitiva, resolvendo assim problemas simples. A linguagem é baseada em JavaScript e possui uma sintaxe simples e intuitiva.


----

## Como Usar

É necessario baixar o requiriments.txt para poder usar a linguagem, nele está contido a biblioteca rply, que é usada para fazer o analisador léxico e sintático da linguagem.

Para baixar o arquivo basta usar o comando:

    pip install -r requirements.txt

Depois é possivel acessar e executar o notebook do jupyer: `solucion_script.ipynb`

Nele você encontrará exemplos de como usar a linguagem e como ela funciona.

Para executar seu próprio código, basta criar um arquivo de texto (exemplos disponiveis: `ex1.txt` , `ex2.txt` e `ex3.txt`) com o seu código e rodar uma célula no fim do notebook seguindo o seguinte exemplo:

    with open('SEU_ARQUIVO.txt', 'r') as f:
        program = f.read()

    symbol = SymbolTable()

        
    arvore = parser.parse(lexer.lex(program))
    arvore.accept(symbol)
    arvore.accept(Decorator(symbol.ST))
    arvore.accept(TypeVerifier())
    arvore.accept(Generator())
    print(SymbolTable.variables)

----

## Gramática
    
    <solucion> ::= <vardecls> <statements>

    <vardecls> ::= <vardecl> <vardecls> | <vardecl>

    <vardecl> ::= <type> <id> | <function>

    <function> ::= funcion <id> ( <params> ) { devolver <expression>; }"

    <type> ::= entero (int) | fraccionario (float)

    <statements> ::= <statement> <statements> | <statement>

    <statement> ::= <atrib> | <ifelse> | <while> | 

    <atrib> ::= <id> = <expression>;

    <ifelse> ::= si ( <expression> <comp> <expression>) { <statements> } sino { <statements> }

    <while> ::= mientras ( <expression> <comp> <expression>) { <statements> }

    <expression> ::= <id> | <number> | <expression> <op> <expression> | ( <expression> )

    <comp> ::= < | > | <= | >= | == | !=

## PARADIGMA FUNCIONAL 

Para definir uma função:

    funcion nome_funcion(param) {
        devolver expression;
    }


Para chamar uma função:

    nome_funcion(param);

A função retorna o valor que pode ser atribuído a uma variável ou usado em uma expressão.

----