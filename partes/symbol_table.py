class Visitor(object):
    pass

class SymbolTable(Visitor):
    def __init__(self):
        self.ST = {}

    def visit_solucion(self, solucion):
        solucion.decls.accept(self)

    def visit_vardecls(self, d):
        d.decl.accept(self)
        if d.decls!=None:
          d.decls.accept(self)

    def visit_vardecl(self, d):
        self.ST[d.id]=d.tp