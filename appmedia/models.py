from django.db import models


class FileModel(models.Model):
    file = models.FileField(upload_to='files')

    class Meta:
        db_table = 'files'
        verbose_name = 'File'
        verbose_name_plural = 'Files'
