from pydantic import BaseModel

class TargetCreate(BaseModel):
    project_id: int
    domain: str

class TargetOut(BaseModel):
    id: int
    project_id: int
    domain: str

    class Config:
        from_attributes = True