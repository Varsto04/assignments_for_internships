from django.shortcuts import render, redirect


def menu(request):
    return render(request, 'menuapp/menu.html')
