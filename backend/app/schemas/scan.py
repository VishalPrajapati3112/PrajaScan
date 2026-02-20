from pydantic import BaseModel

class ScanCreate(BaseModel):
    target_id: int
    scan_type: str  # passive / active

class ScanOut(BaseModel):
    id: int
    target_id: int
    scan_type: str
    status: str

    class Config:
        from_attributes = True