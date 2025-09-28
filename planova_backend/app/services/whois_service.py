#
#
#
#
#
import whois
from datetime import datetime
from typing import Any, Dict, List, Union


def normalize(value: Union[List[Any], Any]) -> Any:
    """Return the first value if it's a list, else return the value as is."""
    if isinstance(value, list):
        return value[0] if value else None
    return value


def format_date(date: Union[datetime, List[datetime], None]) -> Union[str, None]:
    d = normalize(date)
    if isinstance(d, datetime):
        return d.strftime("%Y-%m-%d %H:%M:%S")
    return None


def get_whois_info(domain: str) -> Dict[str, Any]:
    try:
        w = whois.whois(domain)

        return {
            "raw": str(w),  # adaugă output-ul brut WHOIS pentru fallback/debug
            "domain_name": normalize(w.domain_name),
            "tld": normalize(w.tld),
            "registrar": normalize(w.registrar),
            "creation_date": format_date(w.creation_date),
            "expiration_date": format_date(w.expiration_date),
            "updated_date": format_date(w.updated_date),
            "name_servers": w.name_servers if isinstance(w.name_servers, list) else [w.name_servers],
            "status": w.status if isinstance(w.status, list) else [w.status],
            "emails": w.emails if isinstance(w.emails, list) else [w.emails] if w.emails else [],
            "dnssec": normalize(w.dnssec),
            "country": normalize(w.country),
            "org": normalize(w.org),
            "registrant": normalize(w.name),
            "address": normalize(w.address),
        }

    except Exception as e:
        return {"error": f"WHOIS lookup failed: {str(e)}"}
