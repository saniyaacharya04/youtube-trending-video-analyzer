from yt_trending.core.db.session import SessionLocal
from yt_trending.domain.saas_models import Organization

db = SessionLocal()
org = Organization(name="demo-org", api_key="demo-key", plan="free")
db.add(org)
db.commit()
db.close()

print("Demo org created with API key: demo-key")
