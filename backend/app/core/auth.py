import httpx
from fastapi import Depends, HTTPException, Request, status
from clerk_backend_api.security import AuthenticateRequestOptions
from app.core.config import settings
from app.core.clerk import clerk

