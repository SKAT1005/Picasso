from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='files', verbose_name='Файл')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки файла')
    processed = models.BooleanField(default=False, verbose_name='Статус обработки файла')
