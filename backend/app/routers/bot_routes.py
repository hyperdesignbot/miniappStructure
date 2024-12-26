from fastapi import APIRouter
from typing import Optional

from fastapi import Header
from fastapi import Request
from fastapi.responses import JSONResponse
from app.utils.auth import validate_tma_header, authenticator

router = APIRouter()

@router.get("/get_user")
def get_user_instance(request: Request,
                     authorization: Optional[str] = Header(),
                     ):
    print("authorization:",authorization)
    if not validate_tma_header(authorization):
        return JSONResponse(content={"detail": "Invalid 'tma' header"}, status_code=400)
    authorization = authorization.split(" ")[1]
    user = authenticator.get_telegram_user(authorization)
    print("user is:",user)
    return {"user":user}




