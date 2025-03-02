from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

app = FastAPI()

class CodeReviewRequest(BaseModel):
    code: str
    language: str = "python"

@app.post("/review")
async def review_code(request: CodeReviewRequest):
    ast = ASTParser().parse(request.code)
    review = ReviewGenerator().generate_review(request.code, ast)
    return {"review": review, "ast": ast}
