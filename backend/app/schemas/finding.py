from pydantic import BaseModel

class FindingOut(BaseModel):
    id: int
    scan_id: int
    severity: str
    title: str
    description: str | None

    class Config:
        from_attributes = True