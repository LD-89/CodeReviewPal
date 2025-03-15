from core.analysis.ast_parser import ASTParser

code_sample = """
def hello_world():
    print("Hello, world!")
    return True
"""

parser = ASTParser()
ast = parser.parse(code_sample)
print(ast)
