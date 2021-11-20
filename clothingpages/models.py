from django.db import models
from django.db.models.base import Model

# Create your models here.

class items(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    clothingType = models.CharField(max_length=30)
    materialType = models.CharField(max_length=30)
    brandName = models.CharField(max_length=30)
    ownerRating = models.DecimalField(max_digits=2, decimal_places=1)
    memory = models.CharField(max_length=300)

    def __str__(self):
        return(self.firstName + " " + self.lastName + ": " + self.clothingType)

#    def __str__(self):
#       return(self.name_and_item)

#    @property
#   def name_and_item(self):
#        return '%s %s %s' % (self.firstName, self.lastName, self.clothingType)