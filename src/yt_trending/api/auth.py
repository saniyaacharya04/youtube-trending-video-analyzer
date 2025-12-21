from fastapi import Header, HTTPException
from sqlalchemy.orm import Session
from yt_trending.core.db.session import SessionLocal
from yt_trending.domain.saas_models import Organization

def get_org(x_api_key: str = Header(...)):
    db: Session = SessionLocal()
    org = db.query(Organization).filter_by(api_key=x_api_key).first()
    db.close()

    if not org:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return org
