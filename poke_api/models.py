from django.db import models
from django.contrib.auth.models import User

GENDER = (
            ('M', 'Male'),
            ('F', 'Female'),
)


# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    level = models.IntegerField()
    gender = models.CharField(choices=GENDER, max_length=1)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.name + " (" + self.species + ")"
