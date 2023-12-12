#ANALISADOR SINTÁTICO

from syntax_tree import *
from rply import ParserGenerator

def parser_generator():

    pg = ParserGenerator(
    # A list of all token names, accepted by the lexer.
    [
        'OPEN_SOLUCION', 'CLOSE_SOLUCION', 
        'NUMBER', 'PLUS', 'MINUS', 'MUL', 'DIV', 
        'OPEN_PARENS', 'CLOSE_PARENS', 'OPEN_BRACKET', 'CLOSE_BRACKET',

        'VAR', 'INT', 'FLOAT', 'IF', 'ELSE', 'WHILE', 
        'ID', 'COMP','EQUALS', 'SEMICOLOM',
    ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS']),
        ('left', ['MUL', 'DIV'])
    ]
    )

    @pg.production('solucion : OPEN_SOLUCION vardecls statements CLOSE_SOLUCION')
    def prog(p):
        return Solucion(p[1],p[2])

    ##################################################
    # DECLARAÇÕES DE VARIÁVEIS 
    ##################################################

    @pg.production('vardecls : vardecl')
    def vardecls(p):
        return VarDecls(p[0],None)

    @pg.production('vardecls : vardecl vardecls')
    def vardecls(p):
        return VarDecls(p[0],p[1])

    @pg.production('vardecl : VAR INT ID SEMICOLOM')
    def vardecl_int(p):
        return VarDecl(p[2].getstr(), "int")

    @pg.production('vardecl : VAR FLOAT ID SEMICOLOM')
    def vardecl_float(p):
        return VarDecl(p[2].getstr(), "float")

    ##################################################
    # COMANDOS - CASO ABERTO
    ##################################################

    @pg.production('statements : statement')
    def statement_statements(p):
        return Statements(p[0],None)

    @pg.production('statements : statement statements')
    def statement_statements(p):
        return Statements(p[0],p[1])

    @pg.production('statement : ID EQUALS expression SEMICOLOM')
    def statement_atrib(p):
        return Atrib(p[0].getstr(),p[2])

    @pg.production('statement : IF OPEN_PARENS expression COMP expression CLOSE_PARENS OPEN_BRACKET statements CLOSE_BRACKET')
    def expression_ifelse1(p):
        return IfElse (p[2],p[3],p[4],p[7],None)


    @pg.production('statement : IF OPEN_PARENS expression COMP expression CLOSE_PARENS OPEN_BRACKET statements CLOSE_BRACKET ELSE OPEN_BRACKET statements CLOSE_BRACKET')
    def expression_ifelse2(p):
        return IfElse (p[2],p[3],p[4],p[7],p[11])

    @pg.production('statement : WHILE OPEN_PARENS expression COMP expression CLOSE_PARENS OPEN_BRACKET statements CLOSE_BRACKET')
    def statement_while(p):
        return While (p[2],p[3],p[4],p[7])

    @pg.production('expression : ID')
    def expression_id(p):
        return Id(p[0].getstr())

    @pg.production('expression : NUMBER')
    def expression_number(p):
        value = p[0].getstr()

        if "." in value:
            value = float(value)
        else:
            value = int(value)

        return Number(value)

    @pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
    def expression_parens(p):
        return p[1]

    @pg.production('expression : expression PLUS expression')
    @pg.production('expression : expression MINUS expression')
    @pg.production('expression : expression MUL expression')
    @pg.production('expression : expression DIV expression')
    def expression_binop(p):
        left = p[0]
        right = p[2]
        if p[1].gettokentype() == 'PLUS':
            return Add(left, right)
        elif p[1].gettokentype() == 'MINUS':
            return Sub(left, right)
        elif p[1].gettokentype() == 'MUL':
            return Mul(left, right)
        elif p[1].gettokentype() == 'DIV':
            return Div(left, right)
        else:
            raise AssertionError('Oops, this should not be possible!')

    parser = pg.build()
    return parser