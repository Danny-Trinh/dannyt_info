from django.db import models
from django.contrib.auth.models import User
import pokebase as pb


# Create your models here.
class Pokemon(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    species = models.CharField(max_length=30, default='invalid')
    name = models.CharField(max_length=30, default=species)
    level = models.IntegerField(default=0)
    gender = models.CharField(choices=GENDER, max_length=1, default='M')

    pokedata = pb.pokemon(species)

    b_hp = models.IntegerField('base hp', default=0)
    b_defense = models.IntegerField('base defense', default=0)
    b_attack = models.IntegerField('base attack', default=0)
    b_s_defense = models.IntegerField('base special defense', default=0)
    b_s_attack = models.IntegerField('base special attack', default=0)
    b_speed = models.IntegerField('base speed', default=0)

    hp = models.IntegerField(default=b_hp)
    defense = models.IntegerField(default=b_defense)
    attack = models.IntegerField(default=b_attack)
    s_defense = models.IntegerField('special defense', default=b_s_defense)
    s_attack = models.IntegerField('full attack', default=b_s_attack)
    speed = models.IntegerField(default=b_speed)

    iv = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    next_exp = models.IntegerField(default=0)

    def _str_(self):
        return self.name + " (" + self.species + ")"
