from django.db import models

# Create your models here.

class Contactdb(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    subject = models.TextField()

    def __str__(self):
        return self.name