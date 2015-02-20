from bytecodes import bytecodes


class Frame(object):
    def __init__(self):
        self.valuestack = []

    def push(self, value):
        self.valuestack.append(value)

    def pop(self):
        return self.valuestack.pop()


class Interpreter(object):

    def interpret(self, bytecode, frame):
        pc = 0
        while pc < len(bytecode.code):
            opcode = ord(bytecode.code[pc])
            opname = bytecodes[opcode]
            pc = getattr(self, opname)(pc, bytecode, frame)

    def LOAD_CONST(self, pc, bytecode, frame):
        arg = ord(bytecode.code[pc + 1])
        frame.push(bytecode.constants[arg])
        return pc + 2

    def BINARY_ADD(self, pc, bytecode, frame):
        right = frame.pop()
        left = frame.pop()
        frame.push(left.add(right))
        return pc + 1

    def BINARY_SUBTRACT(self, pc, bytecode, frame):
        right = frame.pop()
        left = frame.pop()
        frame.push(left.sub(right))
        return pc + 1

    def BINARY_MULTIPLY(self, pc, bytecode, frame):
        right = frame.pop()
        left = frame.pop()
        frame.push(left.mult(right))
        return pc + 1

    def BINARY_DIVIDE(self, pc, bytecode, frame):
        right = frame.pop()
        left = frame.pop()
        frame.push(left.div(right))
        return pc + 1

    def POP_TOP(self, pc, bytecode, frame):
        frame.pop()
        return pc + 1

    def PRINT(self, pc, bytecode, frame):
        item = frame.pop()
        print item.str()
        return pc + 1
