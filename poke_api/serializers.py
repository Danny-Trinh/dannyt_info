from rest_framework import serializers
from .models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('trainer',
                  'name',

                  'species',
                  'number',

                  'evolve_chain',
                  'gender',

                  'sprite',
                  'level',
                  'iv',

                  'b_hp',
                  'b_defense',
                  'b_attack',
                  'b_s_defense',
                  'b_s_attack',
                  'b_speed',

                  'hp',
                  'defense',
                  'attack',
                  's_defense',
                  's_attack',
                  'speed',

                  'prev_exp',
                  'exp',
                  'next_exp'
                  )
