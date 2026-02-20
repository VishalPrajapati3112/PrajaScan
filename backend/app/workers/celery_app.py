from celery import Celery
from app.core.config import DATABASE_URL
import os

celery = Celery(
    "prajascan",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

# Tell Celery where to find tasks
celery.autodiscover_tasks(["app.workers.tasks"])