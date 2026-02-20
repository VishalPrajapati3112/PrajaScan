from fastapi import APIRouter
from app.api.v1.routes import projects, targets, scans, findings

api_router = APIRouter()
api_router.include_router(projects.router, prefix="/projects", tags=["Projects"])
api_router.include_router(targets.router, prefix="/targets", tags=["Targets"])
api_router.include_router(scans.router, prefix="/scans", tags=["Scans"])
api_router.include_router(findings.router, prefix="/findings", tags=["Findings"])