from langchain.llms import Ollama


class LocalLLMReviewer:
    def __init__(self, model_name="codellama:7b"):
        self.llm = Ollama(model=model_name)

    def generate_review(self, code, ast, embeddings=None):
        prompt = f"""
        Review this Python code:
        ```
        {code}
        ```

        Provide specific feedback on:
        1. Code quality and style issues
        2. Potential bugs or edge cases
        3. Security vulnerabilities
        4. Performance optimizations
        """
        return self.llm.invoke(prompt)
