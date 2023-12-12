from syntax_tree import Expr

class Visitor(object):
    pass

class Generator(Visitor):
    def __init__(self):
        self.result_table = {}
        self.curr_res = []

    def visit_solucion(self, solucion):
        solucion.vardecls.accept(self)
        solucion.stmts.accept(self)

    def visit_vardecls(self, decls):
        decls.vardecl.accept(self)
        if decls.vardecls:
            decls.vardecls.accept(self)

    def visit_vardecl(self, decl):
        self.result_table[decl.id] = None

    def visit_statements(self, stmts):
        stmts.stmt.accept(self)
        if stmts.stmts:
            stmts.stmts.accept(self)
    
    def visit_statement(self, stmt):
        stmt.stmt.accept(self)

    def visit_atrib(self, atrib):
        atrib.expr.accept(self)
        value = self.curr_res.pop()
        self.result_table[atrib.id] = value

    def visit_ifelse(self, ifelse):
        ifelse.expr1.accept(self)
        ifelse.expr2.accept(self)

        e2 = self.curr_res.pop()
        e1 = self.curr_res.pop()

        condition_value = self.evaluate_comp(ifelse.comp, e1, e2)

        if condition_value:
            ifelse.ie1.accept(self)
        elif ifelse.ie2:
            ifelse.ie2.accept(self)
    
    def visit_while(self, w):
        w.expr1.accept(self)
        w.expr2.accept(self)

        e2 = self.curr_res.pop()
        e1 = self.curr_res.pop()

        condition_value = self.evaluate_comp(w.comp, e1, e2)

        while condition_value:
            w.ie1.accept(self)
            w.expr1.accept(self)
            w.expr2.accept(self)

            e2 = self.curr_res.pop()
            e1 = self.curr_res.pop()

            condition_value = self.evaluate_comp(w.comp, e1, e2)
    
    def evaluate_comp(self, comp, left, right):
        comp = comp.getstr()
        if comp == '==':
            return left == right
        elif comp == '!=':
            return left != right
        elif comp == '>=':
            return left >= right
        elif comp == '>':
            return left > right
        elif comp == '<=':
            return left <= right
        elif comp == '<':
            return left < right
        else:
            raise AssertionError('Oops, this should not be possible!')

    
    def visit_number(self, number):
        self.curr_res.append(number.value)
    
    def visit_id(self, id):
        self.curr_res.append(self.result_table[id.value])

    def visit_add(self, add):
        add.left.accept(self)
        add.right.accept(self)
        right_value = self.curr_res.pop()
        left_value = self.curr_res.pop()
        self.curr_res.append(left_value + right_value)

    def visit_sub(self, sub):
        sub.left.accept(self)
        sub.right.accept(self)
        right_value = self.curr_res.pop()
        left_value = self.curr_res.pop()
        self.curr_res.append(left_value - right_value)

    def visit_mul(self, mul):
        mul.left.accept(self)
        mul.right.accept(self)
        right_value = self.curr_res.pop()
        left_value = self.curr_res.pop()
        self.curr_res.append(left_value * right_value)

    def visit_div(self, div):
        div.left.accept(self)
        div.right.accept(self)
        right_value = self.curr_res.pop()
        left_value = self.curr_res.pop()
        self.curr_res.append(left_value / right_value)