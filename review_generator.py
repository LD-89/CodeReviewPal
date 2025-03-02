from transformers import T5ForConditionalGeneration, T5Tokenizer

class ReviewGenerator:
    def __init__(self, model_name="Salesforce/codet5-base-multi-sum"):
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)

    def generate_review(self, code: str, ast: dict) -> str:
        input_text = f"Code: {code}\nAST: {str(ast)}"
        inputs = self.tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
        outputs = self.model.generate(
            inputs.input_ids,
            max_length=256,
            num_beams=4,
            early_stopping=True
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
