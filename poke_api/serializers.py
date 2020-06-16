# todo/serializers.py

from rest_framework import serializers
from .models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('trainer',
                  'name',
                  'species',
                  'level',
                  'gender',
                  'hp',
                  'defense',
                  'attack',
                  's_defense',
                  's_attack',
                  'speed',
                  'iv',
                  'exp',
                  'next_exp'
                  )