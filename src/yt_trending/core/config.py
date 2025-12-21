from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "YouTube Trending Analyzer"
    ENV: str = "local"
    FREE_TIER_LIMIT: int = 50

    class Config:
        env_file = ".env"

settings = Settings()
