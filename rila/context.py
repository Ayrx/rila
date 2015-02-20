class Context(object):
    def __init__(self):
        self.data = []
        self.constants = []

    def new_const(self, const):
        self.constants.append(const)
        return len(self.constants) - 1

    def emit(self, bytecode, arg=0):
        self.data.append(chr(bytecode))
        self.data.append(chr(arg))

    def create_bytecode(self):
        return ByteCode("".join(self.data), self.constants[:])


class ByteCode(object):
    def __init__(self, code, constants):
        self.code = code
        self.constants = constants
