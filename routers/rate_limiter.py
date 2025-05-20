from fastapi import APIRouter, Query
from services.limiter import RateLimiter
from services.limiter import RateLimiter
from services.limiter import Role, RoleTest

from fastapi.responses import JSONResponse

#no prefix too long
#router_current = APIRouter(prefix="/rate")

router_current = APIRouter()
limiter = RateLimiter(3)

@router_current.get("/enum_test")
def handle_enum(role: Role):
    newtest = RoleTest.HIGH
    print(newtest)
    print(newtest.value)

    return JSONResponse(content={"therole": role})

@router_current.get("/request", tags = ["Rate Limiting"])
def handle_request(user: str):
    allowed = limiter.allow_request(user)
    return JSONResponse(content={"user": user, "allowed": allowed})

@router_current.get("/infinite_requests", tags = ["Rate Limiting Infinite"])
def handle_infinite_requests(
    user: str = Query(..., min_length=1),
    number: int = Query(..., gt=0)
):
    allowed = limiter.allow_request(user)
    return JSONResponse(content={"user": user, "allowed": allowed, "number": number})