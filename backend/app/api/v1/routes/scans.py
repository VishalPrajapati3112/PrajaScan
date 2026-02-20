from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.db.models.scan_job import ScanJob
from app.schemas.scan import ScanCreate, ScanOut
from app.workers.tasks.scan_tasks import run_scan

router = APIRouter()

@router.post("/", response_model=ScanOut)
def create_scan(payload: ScanCreate, db: Session = Depends(get_db)):
    scan = ScanJob(
        target_id=payload.target_id,
        scan_type=payload.scan_type,
        status="queued"
    )
    db.add(scan)
    db.commit()
    db.refresh(scan)
    
    run_scan.delay(scan.id)
    
    return scan

@router.get("/", response_model=list[ScanOut])
def list_scans(
    target_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    q = db.query(ScanJob).order_by(ScanJob.id.desc())
    if target_id is not None:
        q = q.filter(ScanJob.target_id == target_id)
    return q.all()