from tree_sitter import Language, Parser

class ASTParser:
    def __init__(self, lang='python'):
        self.lang = Language('./parsers/python.so', lang)
        self.parser = Parser()
        self.parser.set_language(self.lang)

    def parse(self, code: str) -> dict:
        tree = self.parser.parse(bytes(code, 'utf8'))
        return self._walk_tree(tree.root_node)

    def _walk_tree(self, node):
        return {
            'type': node.type,
            'children': [self._walk_tree(child) for child in node.children],
            'text': node.text.decode() if node.text else None,
        }