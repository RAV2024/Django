from django.shortcuts import render
from django.http import HttpResponse
import json
import os
from django.http import Http404
from Django.forms import ContactForm


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def guitars(request):

    json_file_path = os.path.join('data.json')

    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            guitars = json.load(file)
    except FileNotFoundError:
        raise Http404("Data file not found.")
    except json.JSONDecodeError:
        raise Http404("Data file is not valid JSON.")

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price is not None:
        try:
            min_price = float(min_price)
            guitars = [guitar for guitar in guitars if 'price' in guitar and float(guitar['price']) >= min_price]
        except ValueError:
            pass

    if max_price is not None:
        try:
            max_price = float(max_price)
            guitars = [guitar for guitar in guitars if 'price' in guitar and float(guitar['price']) <= max_price]
        except ValueError:
            # Обработка случая, когда max_price не может быть преобразован в float
            pass

    return render(request, "guitars.html", {'guitars': guitars})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Спасибо')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})




#return render(request, "contact.html")


