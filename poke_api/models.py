from django.db import models
from django.contrib.auth.models import User

GENDER = (
            ('M', 'Male'),
            ('F', 'Female'),
)


# Create your models here.
class Pokemon(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    level = models.IntegerField()
    gender = models.CharField(choices=GENDER, max_length=1)
    hp = models.IntegerField()
    defense = models.IntegerField()
    attack = models.IntegerField()
    s_defense = models.IntegerField()
    s_attack = models.IntegerField()
    speed = models.IntegerField()
    iv = models.IntegerField()
    exp = models.IntegerField()
    next_exp = models.IntegerField()




    def _str_(self):
        return self.name + " (" + self.species + ")"
