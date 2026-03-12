from fastapi import APIRouter
from pydantic import BaseModel
from engine.decision_engine import DecisionEngine

router = APIRouter()

decision_engine = DecisionEngine()


class RequestData(BaseModel):
    request_id: int
    income: int
    is_duplicate: bool


@router.post("/process_request")
def process_request(request: RequestData):

    result = decision_engine.process_request(
        request.request_id,
        request.dict()
    )

    return result