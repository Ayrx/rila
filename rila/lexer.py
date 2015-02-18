from rply import LexerGenerator


lg = LexerGenerator()
lg.ignore(r"\s+")
lg.add("NUMBER", r"\d+")
lg.add("ADD", r"\+")
lg.add("SUB", r"\-")
lg.add("MULT", r"\*")
lg.add("DIV", r"\/")
lg.add("SEMICOLON", r";")
lexer = lg.build()
