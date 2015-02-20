import sys

from context import Context
from interpreter import Frame, Interpreter
from lexer import lexer
from parser import parser


def run(fname):
    with open(fname, "r") as f:
        source_code = f.read()

    ctx = Context()
    parser.parse(lexer.lex(source_code)).compile(ctx)

    frame = Frame()
    interpreter = Interpreter()

    interpreter.interpret(ctx.create_bytecode(), frame)


def entry_point(argv):
    try:
        filename = argv[1]

    except IndexError:
        print "Missing argument"
        return 1

    run(filename)
    return 0


def target(*args):
    return entry_point, None


if __name__ == "__main__":
    entry_point(sys.argv)
