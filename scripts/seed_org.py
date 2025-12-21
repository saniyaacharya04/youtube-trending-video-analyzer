from yt_trending.core.db.session import SessionLocal
from yt_trending.domain.saas_models import Organization

db = SessionLocal()

existing = db.query(Organization).filter_by(api_key="demo-key").first()
if existing:
    print("Demo org already exists, skipping seed")
else:
    org = Organization(name="demo-org", api_key="demo-key", plan="free")
    db.add(org)
    db.commit()
    print("Demo org created with API key: demo-key")

db.close()
