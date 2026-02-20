import time
from app.workers.celery_app import celery
from app.db.session import SessionLocal
from app.db.models.scan_job import ScanJob

@celery.task
def run_scan(scan_id: int):
    db = SessionLocal()
    scan = db.query(ScanJob).filter(ScanJob.id == scan_id).first()

    if not scan:
        db.close()
        return

    scan.status = "running"
    db.commit()

    # simulate scan work
    time.sleep(5)

    scan.status = "completed"
    db.commit()
    db.close()