from fastapi import Header

SECRET_KEY = "abc"

def authenticate(token: str = Header(None)):
    if token != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token
