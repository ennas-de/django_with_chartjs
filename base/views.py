from django.shortcuts import render
from .models import Country

def bar(request):
    labels = []
    data = []
    country = Country.objects.order_by('-country')[:5]
    for country_data in country:
        labels.append(country_data.country)
        data.append(country_data.population)
    context = {
        'labels':labels,
        'data':data
    }
    return render(request, 'index.html', context)

def line(request):
    labels = []
    data = []
    country = Country.objects.order_by('-country')[:5]
    for country_data in country:
        labels.append(country_data.country)
        data.append(country_data.population)
    context = {
        'labels':labels,
        'data':data
    }
    return render(request, 'line.html',context)

def bubble(request):
    labels = []
    data = []
    country = Country.objects.order_by('-country')[:5]
    for country_data in country:
        labels.append(country_data.country)
        data.append(country_data.population)
    context = {
        'labels':labels,
        'data':data
    }
    return render(request, 'bubble.html', context)

def doughnut(request):
    labels = []
    data = []
    country = Country.objects.order_by('-country')[:5]
    for country_data in country:
        labels.append(country_data.country)
        data.append(country_data.population)
    context = {
        'labels':labels,
        'data':data
    }
    return render(request, 'doughnut.html',context)

def scatter(request):
    labels = []
    data = []
    country = Country.objects.order_by('-country')[:5]
    for country_data in country:
        labels.append(country_data.country)
        data.append(country_data.population)
    context = {
        'labels':labels,
        'data':data
    }
    return render(request, 'scatter.html',context)

def radar(request):
    labels = []
    data = []
    country = Country.objects.order_by('-country')[:5]
    for country_data in country:
        labels.append(country_data.country)
        data.append(country_data.population)
    context = {
        'labels':labels,
        'data':data
    }
    return render(request, 'radar.html', context)