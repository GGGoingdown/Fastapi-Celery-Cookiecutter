from typing import Dict
from celery import shared_task


@shared_task()
def health_check() -> Dict:
    return {"detail": "health"}
