import httpx
from fastapi import Depends, HTTPException, Request, status
from clerk_backend_api.security import AuthenticateRequestOptions
from app.core.config import settings
from app.core.clerk import clerk

class AuthUser:
    def __init__(self, user_id: str, org_id: str, org_permissions: list):
        self.user_id = user_id
        self.org_id = org_id
        self.org_permissions = org_permissions
    
    def has_permission(self, permission: str) -> bool:
        return permission in self.org_permissions
    
    @property
    def can_view(self) -> bool:
        return self.has_permission("org:tasks:view")
    
    @property
    def can_create(self) -> bool:
        return self.has_permission("org:tasks:create")
    
    @property
    def can_delete(self) -> bool:
        return self.has_permission("org:tasks:delete")
    
    @property
    def can_edit(self) -> bool:
        return self.has_permission("org:tasks:edit")
    
def convert_to_httpx_request(fastapi_request: Request) -> httpx.Request:
    return httpx.Request(
        method=fastapi_request.method,
        url = str(fastapi_request.url),
        headers=dict(fastapi_request.headers)
    )

async def get_current_user(request: Request) -> AuthUser:
    httpx_request = convert_to_httpx_request(request)

    request_state = clerk.authenticate_request(
        httpx_request,
        AuthenticateRequestOptions(authorized_parties=[settings.FRONTEND_URL])
    )