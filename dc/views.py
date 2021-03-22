from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vocal


# Create your views here.
def home(request):
    return render(request, 'dc/home.html')

def explore(request):
    vocals = Vocal.objects.all()
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
            messages.error('Please Enter the Vocals!')

        else:
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


    return render(request, 'dc/home.html')
