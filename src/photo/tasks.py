from celery import shared_task
from datetime import date
from photo.models import Photo


@shared_task
def cheking_sharing_end_date():
    for photo in Photo.objects.all():
        if photo.sharing_end_date <= date.today():
            photo.update(sharing = False)
