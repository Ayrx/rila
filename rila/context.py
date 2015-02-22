class Context(object):
    def __init__(self):
        self.data = []
        self.constants = []
        self.variables = []
        self.variables_index = {}

    def new_const(self, const):
        self.constants.append(const)
        return len(self.constants) - 1

    def new_var(self, var):
        try:
            return self.variables_index[var]
        except KeyError:
            self.variables_index[var] = len(self.variables)
            self.variables.append(var)
            return len(self.variables) - 1

    def emit(self, bytecode, arg=0):
        self.data.append(chr(bytecode))
        self.data.append(chr(arg))

    def create_bytecode(self):
        return ByteCode(
            "".join(self.data), self.constants[:], len(self.variables)
        )


class ByteCode(object):
    def __init__(self, code, constants, num_variables):
        self.code = code
        self.constants = constants
        self.num_variables = num_variables
