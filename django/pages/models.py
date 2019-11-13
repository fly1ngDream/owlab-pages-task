from django.db import models

import uuid


class VersionsThread(models.Model):
    def __str__(self):
        return str(self.id)


class Page(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    versions_thread = models.ForeignKey(
        VersionsThread,
        related_name='pages',
        on_delete=models.DO_NOTHING,
    )
    version = models.FloatField(default=1.0)
    is_current = models.BooleanField(default=True)

    class Meta:
        unique_together = (
            'versions_thread',
            'version',
        )
        ordering = (
            '-versions_thread',
            '-version',
        )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.disable_current()
        super().save(*args, **kwargs)

    def disable_current(self):
        current = self.versions.filter(
            is_current=True,
        ).first()
        if current and self != current:
            current.is_current = False
            current.save()

    @property
    def versions(self):
        return self.__class__.objects.filter(versions_thread=self.versions_thread)

    def make_current(self):
        self.disable_current()
        self.is_current = True
        self.save()
