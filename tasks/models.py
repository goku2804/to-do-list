from django.db import models

class Task(models.Model):
    subject = models.CharField(max_length=200)
    notes = models.TextField()

    def __str__(self):
        return self.subject
