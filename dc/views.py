from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vocal
import random


# Create your views here.

success_messages = [
    'Wow! I liked it. Let\'s go for one more.',
    'Yeah! Thanks for uploading.',
    'I really appreciate it. It helps dude!',
    'Oooo... I like your taste.'
    'Just Amazing, let\'s do that again.',
    'Your music is as good as you! I want more of it.',
]

def home(request):
    return render(request, 'dc/home.html')

def explore(request):
    vocals = Vocal.objects.all().order_by('-id')
    return render(request, 'dc/explore.html', {'vocals': vocals})

def upload(request):
    if request.method == 'POST':
        file = False
        try:
            request.POST['vocal_file']

        except:
            file = True

        vocal_url = request.POST['vocal_url']
        if len(vocal_url) < 2 and not file:
            print('I got in!')
            messages.error(request, 'Please Enter the Vocals!')

        else:
            messages.success(request, random.choices(success_messages)[0])
            if len(vocal_url) > 2:
                vocal = Vocal(
                        email = request.POST['email'],
                        song_name = request.POST['name'],
                        song_url = request.POST['song_url'],
                        vocal_url = vocal_url,
                    )
                vocal.save()

            else:
                vocal = Vocal(
                        email = request.POST['email'],
                        song_name = request.POST['name'],
                        song_url = request.POST['song_url'],
                        vocal = request.FILES['vocal_file'],
                    )
                vocal.save()


    return redirect('home')
