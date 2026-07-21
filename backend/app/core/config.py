import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd=True))

class Config:
    CLERK_SECRET_KEY: str = os.getenv("CLERK_SECRET_KEY", "")
    CLERK_PUBLISHABLE_KEY: str = os.getenv("CLERK_PUBLISHABLE", "")
    CLERK_WEBHOOK_SECRET: str = os.getenv("CLERK_WEBHOOK_SECRET", "")
    CLERK_JWKS_URL: str = os.getenv("CLERK_JWKS_URL", "")

    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./taskboard.db")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", os.getenv("FRONTENT_URL", "http://localhost:5173"))

    FREE_TIER_MEMBERSHIP_LIMIT: int = 2
    PRO_TIER_MEMBERSHIP_LIMIT = 0


settings = Config()