from starlette.responses import JSONResponse
from fastapi import Request

import secrets
import os


async def api_authenticate_key(request: Request, call_next):
    API_KEY = request.headers.get("X-API-KEY", "")
    OUR_API_KEY = os.getenv("AUTHENTICATED_KEY", "")

    print(secrets.compare_digest(API_KEY, OUR_API_KEY))

    if not secrets.compare_digest(API_KEY, OUR_API_KEY):
        return JSONResponse(
            status_code=403,
            content={
                "message": "UnAuthorize Request"
            }
        )
    return await call_next(request)