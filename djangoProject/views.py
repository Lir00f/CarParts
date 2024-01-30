from django.shortcuts import render, get_object_or_404
from .models import CarBrand, CarPart

def index(request):
    car_brands = CarBrand.objects.all()
    return render(request, 'index.html', {'car_brands': car_brands})

def car_brand_parts(request, brand_id):
    car_brand = CarBrand.objects.get(pk=brand_id)
    parts = CarPart.objects.filter(brand=car_brand)
    return render(request, 'car_brand_parts.html', {'car_brand': car_brand, 'parts': parts})

def car_part_detail(request, part_id):
    part = get_object_or_404(CarPart, pk=part_id)
    car_brand = part.brand
    return render(request, 'car_part_detail.html', {'part': part, 'car_brand': car_brand})
