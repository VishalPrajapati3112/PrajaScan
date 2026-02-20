import requests
from app.workers.celery_app import celery
from app.db.session import SessionLocal
from app.db.models.scan_job import ScanJob
from app.db.models.target import Target
from app.db.models.finding import Finding

@celery.task
def run_scan(scan_id: int):
    db = SessionLocal()
    scan = db.query(ScanJob).filter(ScanJob.id == scan_id).first()

    if not scan:
        db.close()
        return

    scan.status = "running"
    db.commit()

    target = db.query(Target).filter(Target.id == scan.target_id).first()
    if not target:
        scan.status = "failed"
        db.commit()
        db.close()
        return

    try:
        response = requests.get(f"http://{target.domain}", timeout=5)
        headers = response.headers

        # Check security headers
        if "X-Frame-Options" not in headers:
            finding = Finding(
                scan_id=scan.id,
                severity="medium",
                title="Missing X-Frame-Options Header",
                description="The application does not set X-Frame-Options header."
            )
            db.add(finding)

        if "Content-Security-Policy" not in headers:
            finding = Finding(
                scan_id=scan.id,
                severity="medium",
                title="Missing Content-Security-Policy Header",
                description="The application does not define a Content Security Policy."
            )
            db.add(finding)

        db.commit()

        scan.status = "completed"
        db.commit()

    except Exception:
        scan.status = "failed"
        db.commit()

    db.close()