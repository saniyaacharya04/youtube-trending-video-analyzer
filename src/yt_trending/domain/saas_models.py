from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    api_key = Column(String, unique=True)
    plan = Column(String, default="free")


class UsageMetric(Base):
    __tablename__ = "usage_metrics"

    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(Integer)
    endpoint = Column(String)
    count = Column(Integer, default=0)
