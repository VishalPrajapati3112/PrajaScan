from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.db.models.target import Target
from app.schemas.target import TargetCreate, TargetOut

router = APIRouter()

@router.post("/", response_model=TargetOut)
def create_target(payload: TargetCreate, db: Session = Depends(get_db)):
    target = Target(project_id=payload.project_id, domain=payload.domain)
    db.add(target)
    db.commit()
    db.refresh(target)
    return target

@router.get("/", response_model=list[TargetOut])
def list_targets(
    project_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    q = db.query(Target).order_by(Target.id.desc())
    if project_id is not None:
        q = q.filter(Target.project_id == project_id)
    return q.all()