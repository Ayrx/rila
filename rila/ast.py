from rply.token import BaseBox

from rila import bytecodes
from rila.objects import RilaNumber


class Node(BaseBox):
    pass


class Block(Node):
    def __init__(self, statements):
        self.statements = statements

    def compile(self, ctx):
        for i in self.statements:
            i.compile(ctx)


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
        }
        ctx.emit(opname[self.operator])
