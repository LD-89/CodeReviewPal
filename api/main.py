from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

from core.ai.local_llm import LocalLLMReviewer
from core.analysis.ast_parser import ASTParser
from core.analysis.pipeline import CodeAnalysisPipeline

app = FastAPI()

class CodeReviewRequest(BaseModel):
    code: str
    language: str = "python"

@app.post("/review")
async def review_code(request: CodeReviewRequest):
    pipeline = CodeAnalysisPipeline(
        parser=ASTParser(),
        embedder=None,
        reviewer=LocalLLMReviewer()
    )
    review = pipeline.analyze(request.code, request.language)
    return {"review": review}
