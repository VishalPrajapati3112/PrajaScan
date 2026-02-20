from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.db.models.finding import Finding
from app.schemas.finding import FindingOut

router = APIRouter()

@router.get("/", response_model=list[FindingOut])
def list_findings(
    scan_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    q = db.query(Finding).order_by(Finding.id.desc())
    if scan_id is not None:
        q = q.filter(Finding.scan_id == scan_id)
    return q.all()