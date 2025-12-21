from yt_trending.core.db.session import engine
from yt_trending.domain.saas_models import Base

Base.metadata.create_all(bind=engine)
print("Database initialized")
