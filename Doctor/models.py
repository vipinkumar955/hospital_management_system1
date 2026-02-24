from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    office = models.CharField(max_length=200)
    years_experience = models.IntegerField()
    profile_image = models.ImageField(upload_to='doctors/', null=True, blank=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_choices = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
    ]
    day = models.CharField(max_length=3, choices=day_choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.day}"

class Bio(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    bio_text = models.TextField()

    def __str__(self):
        return f"{self.doctor.name} Bio"