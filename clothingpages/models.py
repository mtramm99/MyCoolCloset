from django.db import models
from django.db.models.base import Model

# Create your models here.

class items(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    clothingType = models.CharField(max_length=30)
    materialType = models.CharField(max_length=30)
    brandName = models.CharField(max_length=30)
    ownerRating = models.DecimalField(2, 1)
    memory = models.CharField(max_length=300)

    def __str__(self):
        return(self.firstName + " " + self.lastName + ": " + self.clothingType)