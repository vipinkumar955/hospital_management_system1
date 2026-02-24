from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True)   # Automatic ID

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
    )

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return self.name