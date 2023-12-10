from django.db import models

# Create your models here.

class Phonebook(models.Model):
    Name = models.CharField(max_length=20)
    Number = models.CharField(max_length=20)

def __str__(self):
    return f" {self.Name}{self.Number}"

