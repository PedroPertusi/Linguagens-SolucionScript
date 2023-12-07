from rply import LexerGenerator

def lexer_generator():

    lg = LexerGenerator()

    lg.add('OPEN_SOLUCION', r'<solucion>')
    lg.add('CLOSE_SOLUCION', r'</solucion>')


    lg.add('NUMBER', r'\d+(.\d+)?')
    lg.add('PLUS', r'\+')
    lg.add('MINUS', r'-')
    lg.add('MUL', r'\*')
    lg.add('DIV', r'/')

    lg.add('OPEN_PARENS', r'\(')
    lg.add('CLOSE_PARENS', r'\)')
    lg.add('OPEN_BRACKET', r'\{')
    lg.add('CLOSE_BRACKET', r'\}')


    lg.add('VAR', r'var')
    lg.add('INT', r'int')
    lg.add('FLOAT', r'float')
    lg.add('IF', r'si')
    lg.add('ELSE', r'sino')
    lg.add('WHILE', r'mientras')

    lg.add('ID', r'[a-zA-Z][a-zA-Z0-9]*')
    lg.add('COMP', r'==|!=|<=|>=|<|>')
    lg.add('EQUALS', r'=')
    lg.add('SEMICOLOM', r'\;')

    lg.ignore(r'\s+') # ignore spaces
    # lg.ignore(r'//.*') # ignore comments
    # lg.ignore(r'/\*.*\*/') # ignore comments
    lg.ignore(r'\n+') # ignore newlines


    lexer = lg.build()
    return lexer
