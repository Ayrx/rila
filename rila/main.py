import sys

from context import Context
from interpreter import Frame, Interpreter
from lexer import lexer
from parser import parser


def run(fname):
    with open(fname, "r") as f:
        source_code = f.read()

    if source_code[0:2] == "#!":
        source_code = "\n".join(source_code.split("\n")[1:])

    ctx = Context()
    parser.parse(lexer.lex(source_code)).compile(ctx)

    bytecode = ctx.create_bytecode()
    frame = Frame(bytecode)
    interpreter = Interpreter()

    interpreter.interpret(bytecode, frame)


def entry_point(argv):
    try:
        filename = argv[1]

    except IndexError:
        print "Please specify a source file."
        return 1

    run(filename)
    return 0


def target(*args):
    return entry_point, None


if __name__ == "__main__":
    entry_point(sys.argv)
