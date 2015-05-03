from rply import LexerGenerator


lg = LexerGenerator()
lg.ignore(r"\s+")
lg.add("NUMBER", r"\d+")
lg.add("BOOLEAN", r"True|False")
lg.add("ADD", r"\+")
lg.add("SUB", r"\-")
lg.add("MULT", r"\*")
lg.add("DIV", r"\/")
lg.add("SEMICOLON", r";")
lg.add("PRINT", r"print")
lg.add("NAME", r"[a-zA-Z_][a-zA-Z0-9_]*")
lg.add("ASSIGN", r"=")
lexer = lg.build()
