from rply.token import BaseBox

import bytecodes
from objects import RilaBoolean, RilaNumber


class Node(BaseBox):
    pass


class Block(Node):
    def __init__(self, statements):
        self.statements = statements

    def compile(self, ctx):
        for i in self.statements:
            i.compile(ctx)

    def getastlist(self):
        return self.statements


class Statement(Node):
    def __init__(self, expression):
        self.expression = expression

    def compile(self, ctx):
        self.expression.compile(ctx)
        ctx.emit(bytecodes.POP_TOP)


class Number(Node):
    def __init__(self, value):
        self.value = value

    def compile(self, ctx):
        ctx.emit(bytecodes.LOAD_CONST, ctx.new_const(RilaNumber(self.value)))


class BinaryOp(BaseBox):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def compile(self, ctx):
        self.left.compile(ctx)
        self.right.compile(ctx)
        opname = {
            "+": bytecodes.BINARY_ADD,
            "-": bytecodes.BINARY_SUBTRACT,
            "*": bytecodes.BINARY_MULTIPLY,
            "/": bytecodes.BINARY_DIVIDE,
            "==": bytecodes.BINARY_EQUALS,
        }
        ctx.emit(opname[self.operator])


class Print(Node):
    def __init__(self, expression):
        self.expression = expression

    def compile(self, ctx):
        self.expression.compile(ctx)
        ctx.emit(bytecodes.PRINT)


class Name(Node):
    def __init__(self, name):
        self.name = name

    def compile(self, ctx):
        ctx.emit(bytecodes.LOAD_NAME, ctx.new_var(self.name))


class Assignment(Node):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def compile(self, ctx):
        self.expression.compile(ctx)
        ctx.emit(bytecodes.STORE_NAME, ctx.new_var(self.name))


class Boolean(Node):
    def __init__(self, value):
        self.value = value

    def compile(self, ctx):
        ctx.emit(bytecodes.LOAD_CONST, ctx.new_const(RilaBoolean(self.value)))
