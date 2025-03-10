from django.db import models
from django.utils import timezone

class ActiveManager(models.Manager):
    # Project.objects.get_queryset() === Project.objects.all()
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Project.Status.ACTIVE)
        )
class Project(models.Model):
    class Status(models.TextChoices):
        NOT_STARTED = 'NOS','Not Started'
        ACTIVE = 'ACT','Active'
        COMPLETED = 'COM','Completed'
        CANCELLED = 'CAN','Cancelled'
        ON_HOLD = 'ONH','On Hold'



    name = models.CharField(max_length=20)
    description= models.TextField(max_length=255)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(default=timezone.now)
    budget = models.FloatField()
    status = models.CharField(
        max_length=3,
        choices = Status.choices,
        default=Status.NOT_STARTED
    )
    objects = models.Manager()
    active = ActiveManager()

    def __str__(self):
        return f'{self.name}-{self.status}'
    class Meta:
        ordering = ['-startDate']
        indexes = [
            models.Index(fields=['-startDate'],)
        ]