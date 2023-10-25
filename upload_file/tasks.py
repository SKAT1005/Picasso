from celery import shared_task
from .models import File

@shared_task
def process_file_task(file_id):
    file_instance = File.objects.get(id=file_id)
    file_instance.processed = True
    file_instance.save()