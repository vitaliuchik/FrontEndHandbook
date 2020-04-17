from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'handbook/index.html')


def text(request):
    return render(request, 'handbook/text.html')


def tables(request):
    return render(request, 'handbook/tables.html')

def forms(request):
    return render(request, 'handbook/forms.html')


def images(request):
    return render(request, 'handbook/images.html')


def media(request):
    return render(request, 'handbook/media.html')


def svg(request):
    return render(request, 'handbook/svg.html')


def animation(request):
    return render(request, 'handbook/animation.html')


def contact(request):
    return render(request, 'handbook/contact.html')