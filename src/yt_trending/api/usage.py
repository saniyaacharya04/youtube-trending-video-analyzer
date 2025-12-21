from fastapi import HTTPException
from sqlalchemy.orm import Session
from yt_trending.core.db.session import SessionLocal
from yt_trending.domain.saas_models import UsageMetric

FREE_LIMIT = 5

def track_usage(org_id: int, endpoint: str):
    db: Session = SessionLocal()

    usage = db.query(UsageMetric).filter_by(
        org_id=org_id,
        endpoint=endpoint
    ).first()

    if not usage:
        usage = UsageMetric(org_id=org_id, endpoint=endpoint, count=0)
        db.add(usage)

    usage.count += 1

    if usage.count > FREE_LIMIT:
        db.close()
        raise HTTPException(status_code=403, detail="Free tier limit exceeded")

    db.commit()
    db.close()
