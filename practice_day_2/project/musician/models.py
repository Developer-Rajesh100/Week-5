from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    instrument_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.email} | {self.phone_number} | {self.instrument_type}"