from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.services.whois_service import get_whois_info

router = APIRouter()

@router.get("/")
async def whois_lookup(domain: str, current_user: dict = Depends(get_current_user)):
    data = get_whois_info(domain)
    return {
        "domain": domain,
        "user": current_user["username"],
        "whois": data
    }
