from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class ScanJob(Base):
    __tablename__ = "scan_jobs"

    id = Column(Integer, primary_key=True, index=True)
    target_id = Column(Integer, ForeignKey("targets.id"), nullable=False)
    scan_type = Column(String(50), nullable=False)  # passive / active
    status = Column(String(50), nullable=False, default="queued")
    created_at = Column(DateTime(timezone=True), server_default=func.now())