class CodeAnalysisPipeline:
    def __init__(self, parser, embedder, reviewer):
        self.parser = parser
        self.embedder = embedder
        self.reviewer = reviewer

    def analyze(self, code_snippet, language="python"):
        ast = self.parser.parse(code_snippet, language)
        embeddings = self.embedder.embed(code_snippet)
        review = self.reviewer.generate_review(code_snippet, ast, embeddings)
        return review
