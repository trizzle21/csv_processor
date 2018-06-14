from django.db import models
from django.contrib.postgres.fields import JSONField

from django.utils import timezone


class CSVImportRecord(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    customer = models.TextField()
    errors = models.TextField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CSVExportLog, self).save(*args, **kwargs)

