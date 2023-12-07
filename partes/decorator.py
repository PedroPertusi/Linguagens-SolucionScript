class Visitor(object):
    pass

from syntax_tree import Expr

class Decorator(Visitor):

    def __init__(self, ST):
        self.ST = ST

    def visit_solucion(self, i):
        i.stmts.accept(self)

    def visit_statements(self, d):
        d.stmt.accept(self)
        if d.stmts!=None:
          d.stmts.accept(self)

    def visit_statement(self, d):
        d.stmt.accept(self)

    def visit_atrib(self, i):
        if i.id in self.ST:
          i.decor_type=self.ST[i.id]
        else:
          raise AssertionError('id not declared')
        i.expr.accept(self)

    def visit_ifelse(self, i):
        i.expr1.accept(self)
        i.expr2.accept(self)
        i.ie1.accept(self)
        if i.ie2!=None:
          i.ie2.accept(self)

    def visit_while(self, i):
        i.expr1.accept(self)
        i.expr2.accept(self)
        i.ie1.accept(self)


    def visit_id(self, i):
        if i.value in self.ST:
          i.decor_type=self.ST[i.value]
        else:
          raise AssertionError('id not declared')


    def visit_number(self, i):
        if "." in str(i.value):
          i.decor_type='float'
        else:
          i.decor_type='int'


    def visit_add(self, a):
        a.left.accept(self)
        a.right.accept(self)
        if a.left.decor_type=="float" or a.right.decor_type=="float":
          a.decor_type="float"
        else:
          a.decor_type="int"


    def visit_sub(self, a):
        a.left.accept(self)
        a.right.accept(self)
        if a.left.decor_type=="float" or a.right.decor_type=="float":
          a.decor_type="float"
        else:
          a.decor_type="int"

    def visit_mul(self, a):
        a.left.accept(self)
        a.right.accept(self)
        if a.left.decor_type =="float" or a.right.decor_type=="float":
          a.decor_type="float"
        else:
          a.decor_type="int"

    def visit_div(self, a):
        a.left.accept(self)
        a.right.accept(self)
        if a.left.decor_type=="float" or a.right.decor_type=="float":
          a.decor_type="float"
        else:
          a.decor_type="int"