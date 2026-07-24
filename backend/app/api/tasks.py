from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.core.auth import AuthUser, get_current_user, require_view, require_create, require_delete
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskStatusUpdate, TaskResponse

router = APIRouter(prefix="/api/tasks", tags="tasks")


@router.get("", response_model=List[TaskResponse])
def list_tasks(user: AuthUser = Depends(require_view), db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.org_id == user.org_id).all()
    return tasks

@router.post("", response_model=TaskResponse)
def create_task(task_data: TaskCreate, user: AuthUser = Depends(require_create), db: Session = Depends(get_db)):
    pass