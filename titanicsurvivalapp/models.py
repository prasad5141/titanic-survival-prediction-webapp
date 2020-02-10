from django.db import models

# Create your models here.
class History(models.Model):
    Gender_choice = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )
    BerthClasses = (
        (1, 'Class 1'),
        (2, 'Class 2'),
        (3, 'Class 3')
    )
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=Gender_choice)
    passenger_class = models.CharField(max_length=1, choices=BerthClasses)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    survived = models.BooleanField(null=False, blank=False)