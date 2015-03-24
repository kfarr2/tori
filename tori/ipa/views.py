from django.shortcuts import render
from .models import Character, Vowel, Consonant

def ipa(request):
    characters = Character.objects.all()
    return render(request, 'ipa/ipa.html', {
        'characters': characters,
    })

def _list(request):
    characters = Character.objects.all()
    vowels = Vowel.objects.all()
    consonants = Consonant.objects.all()

    return render(request, 'ipa/list.html', {
        'characters': characters,
        'vowels': vowels,
        'consonants': consonants,
    })

def create(request):
    return _edit(request, char_id=None)

def edit(request, char_id):
    return _edit(request, char_id)

def _edit(request, char_id):
    pass
