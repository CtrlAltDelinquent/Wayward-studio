from django.shortcuts import render
from django.http import HttpResponse

def games_list(request):
    return HttpResponse("Finished games list")

def game_detail(request, slug):
    return HttpResponse(f"Game detail placeholder for game: {slug}")
