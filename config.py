from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    COINDCX_API_KEY: str
    COINDCX_SECRET_KEY: str
    COINDCX_BASE_URL: str = "https://api.coindcx.com"
    DRY_RUN: bool = True

    class Config:
        env_file = ".env"

settings = Settings()