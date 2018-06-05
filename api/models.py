from django.db import models
from django.contrib.postgres.fields import JSONField

from django.utils import timezone


class JSONImportLog(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    data = JSONField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(JSONImportLog, self).save(*args, **kwargs)


class CSVExportLog(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    errors = models.TextField()
    data = JSONField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(JSONImportLog, self).save(*args, **kwargs)

