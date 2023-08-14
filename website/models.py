from django.db import models


# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)
    # finish_until = models.DateTimeField()
    task_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    finish_until = models.DateTimeField()
    created_by = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.task_name}: {self.description}")
