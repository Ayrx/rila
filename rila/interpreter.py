from rpython.rlib.objectmodel import specialize

from bytecodes import bytecodes, unrolled_bytecodes


class Frame(object):
    def __init__(self, bytecode):
        self.valuestack = []
        self.variables = [None] * bytecode.num_variables

    def push(self, value):
        self.valuestack.append(value)

    def pop(self):
        return self.valuestack.pop()


class Interpreter(object):

    def interpret(self, bytecode, frame):
        pc = 0
        while pc < len(bytecode.code):
            opcode = ord(bytecode.code[pc])
            for i, name in unrolled_bytecodes:
                if i == opcode:
                    pc = self.run_instructions(name, pc, bytecode, frame)
                    break

    @specialize.arg(1)
    def run_instructions(self, opname, pc, bytecode, frame):
        return getattr(self, opname)(pc, bytecode, frame)

    def LOAD_CONST(self, pc, bytecode, frame):
        arg = ord(bytecode.code[pc + 1])
        frame.push(bytecode.constants[arg])
        return pc + 2

    def BINARY_ADD(self, pc, bytecode, frame):
        right = frame.pop()
        left = frame.pop()
        frame.push(left.add(right))
        return pc + 2

    def BINARY_SUBTRACT(self, pc, bytecode, frame):
        right = frame.pop()
        left = frame.pop()
        frame.push(left.sub(right))
        return pc + 2

    def BINARY_MULTIPLY(self, pc, bytecode, frame):
        right = frame.pop()
        left = frame.pop()
        frame.push(left.mult(right))
        return pc + 2

    def BINARY_DIVIDE(self, pc, bytecode, frame):
        right = frame.pop()
        left = frame.pop()
        frame.push(left.div(right))
        return pc + 2

    def POP_TOP(self, pc, bytecode, frame):
        frame.pop()
        return pc + 2

    def PRINT(self, pc, bytecode, frame):
        item = frame.pop()
        print item.str()
        return pc + 2

    def STORE_NAME(self, pc, bytecode, frame):
        arg = ord(bytecode.code[pc + 1])
        frame.variables[arg] = frame.pop()
        return pc + 2

    def LOAD_NAME(self, pc, bytecode, frame):
        arg = ord(bytecode.code[pc + 1])
        frame.push(frame.variables[arg])
        return pc + 2
