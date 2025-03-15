import sys
from core.analysis.pipeline import CodeAnalysisPipeline
from core.analysis.ast_parser import ASTParser
from core.ai.local_llm import LocalLLMReviewer


def main():
    changed_files = sys.argv[1:]
    pipeline = CodeAnalysisPipeline(
        parser=ASTParser(),
        embedder=None,  # Implement later
        reviewer=LocalLLMReviewer()
    )

    for file in changed_files:
        if not file.endswith('.py'):
            continue

        with open(file, 'r') as f:
            code = f.read()
            analysis = pipeline.analyze(code)
            print(f"Review for {file}:\n{analysis}")


if __name__ == "__main__":
    main()
