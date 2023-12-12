# get the arguments from the command line

import sys
import os

from partes.generator import Generator
from partes.symbol_table import SymbolTable
from partes.decorator import Decorator
from partes.type_verifier import TypeVerifier
from partes.lexer_generator import lexer_generator
from partes.parser import parser_generator

def main():

    if len(sys.argv) != 2:
        print("Uso: python main.py <nome_do_arquivo>")
        return
    
    filename = sys.argv[1]

    if not os.path.exists(filename):
        print("Erro: Arquivo '%s' não econtrado" % filename)
        return
    
    with open(filename) as f:
        prog = f.read()
    
    lexer = lexer_generator()
    parser = parser_generator()
 
    generator = Generator()
    symbol_table = SymbolTable()

    arvore = parser.parse(lexer.lex(prog))
    arvore.accept(symbol_table)
    arvore.accept(Decorator(symbol_table.ST))
    arvore.accept(TypeVerifier())
    arvore.accept(generator)

    print("Result:")
    print(generator.result_table)

if __name__ == '__main__':
    main()