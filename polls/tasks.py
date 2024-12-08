from celery import shared_task
from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)

@shared_task
def delete_expired_paste(paste_id):
    from .models import Paste
    try:
        paste = Paste.objects.get(id=paste_id)
        if paste.expires_at and paste.expires_at <= now():
            paste.delete()
            logger.info(f"Deleted paste with ID {paste_id} as it expired.")
        else:
            logger.info(f"Paste with ID {paste_id} has not expired yet.")
    except Paste.DoesNotExist:
        logger.warning(f"Paste with ID {paste_id} does not exist.")