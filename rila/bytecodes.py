import sys

from rpython.rlib.unroll import unrolling_iterable

bytecodes = [
    "LOAD_CONST",
    "BINARY_ADD",
    "BINARY_SUBTRACT",
    "BINARY_MULTIPLY",
    "BINARY_DIVIDE",
    "POP_TOP",
    "PRINT",
]

bytecode_names = []

module = sys.modules[__name__]
for i, name in enumerate(bytecodes):
    setattr(module, name, i)
    bytecode_names.append(name)

unrolled_bytecodes = unrolling_iterable(enumerate(bytecode_names))
