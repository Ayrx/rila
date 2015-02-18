import sys


bytecodes = [
    "LOAD_CONST",
    "BINARY_ADD",
    "BINARY_SUBTRACT",
    "BINARY_MULTIPLY",
    "BINARY_DIVIDE",
    "POP_TOP",
]

module = sys.modules[__name__]
for i, name in enumerate(bytecodes):
    setattr(module, name, i)
