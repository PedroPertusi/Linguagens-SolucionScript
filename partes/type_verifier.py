class Visitor(object):
    pass

from syntax_tree import Expr

class TypeVerifier(Visitor):

    def visit_solucion(self, i):
        i.stmts.accept(self)

    def visit_statements(self, d):
        d.stmt.accept(self)
        if d.stmts!=None:
          d.stmts.accept(self)

    def visit_statement(self, d):
        d.stmt.accept(self)

    def visit_atrib(self, i):
        if i.decor_type!=i.expr.decor_type:
          raise AssertionError('type error')

    def visit_ifelse(self, i):
        pass

    def visit_while(self, i):
        pass