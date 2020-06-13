from django.shortcuts import render
import requests


# Create your views here.
def pokemon_view(request):
    resp = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
    # if resp.status_code != 200:
    #     # This means something went wrong.
    #     raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    print(resp.status_code)
    return render(request, 'pokemon/home.html')

