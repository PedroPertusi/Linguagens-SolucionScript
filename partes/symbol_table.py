class Visitor(object):
    pass

class SymbolTable(Visitor):
    def __init__(self):
        self.ST = {}

    def visit_solucion(self, solucion):
        solucion.vardecls.accept(self)

    def visit_vardecls(self, d):
        d.vardecl.accept(self)
        if d.vardecls!=None:
          d.vardecls.accept(self)

    def visit_vardecl(self, d):
        self.ST[d.id]=d.tp