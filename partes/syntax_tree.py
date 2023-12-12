#ÁRVORE SINTÁTICA PREPARADA PARA RECEBER VISITORS

from rply.token import BaseBox

class Solucion(BaseBox):
    def __init__(self, decls,stmts):
        self.vardecls = decls
        self.stmts = stmts

    def accept(self, visitor):
        visitor.visit_solucion(self)

class VarDecls(BaseBox):
    def __init__(self, decl,decls):
        self.vardecl = decl
        self.vardecls = decls

    def accept(self, visitor):
        visitor.visit_vardecls(self)

class VarDecl(BaseBox):
    def __init__(self, id,tp):
        self.id = id
        self.tp = tp

    def accept(self, visitor):
        visitor.visit_vardecl(self)

class Statements(BaseBox):
    def __init__(self, stmt,stmts):
        self.stmt = stmt
        self.stmts = stmts

    def accept(self, visitor):
        visitor.visit_statements(self)

class Statement(BaseBox):
    def __init__(self,stmt):
        self.stmt = stmt

    def accept(self, visitor):
        visitor.visit_statement(self)

class Atrib(BaseBox):
    def __init__(self, id,expr):
        self.id = id
        self.expr = expr

    def accept(self, visitor):
        visitor.visit_atrib(self)

class IfElse(BaseBox):
    def __init__(self, expr1, comp, expr2, ie1,ie2):
        self.expr1=expr1
        self.comp = comp
        self.expr2=expr2
        self.ie1=ie1
        self.ie2=ie2

    def accept(self, visitor):
        visitor.visit_ifelse(self)


class While(BaseBox):
    def __init__(self, expr1, comp, expr2, ie1):
        self.expr1=expr1
        self.comp = comp
        self.expr2=expr2
        self.ie1=ie1


    def accept(self, visitor):
        visitor.visit_while(self)

class Expr(BaseBox):
    def accept(self, visitor):
        method_name = 'visit_{}'.format(self.__class__.__name__.lower())
        visit = getattr(visitor, method_name)
        visit(self)

class Id(Expr):
    def __init__(self, value):
        self.value = value

class Number(Expr):
    def __init__(self, value):
        self.value = value


class BinaryOp(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
  pass


class Sub(BinaryOp):
  pass


class Mul(BinaryOp):
  pass


class Div(BinaryOp):
  pass
