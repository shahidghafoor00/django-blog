from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

posts = [
    {
        'author': 'John Doe',
        'title': 'Codebase',
        'content': 'Successor byteShaft',
        'date_posted': 'March 3, 2020'
    },

    {
        'author': 'Jane Doe',
        'title': 'byteShaft',
        'content': 'Software Services Provider',
        'date_posted': 'March 1, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About is'})
