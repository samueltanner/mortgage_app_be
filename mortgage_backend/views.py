from django.shortcuts import render
from django.contrib import admin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from finny_scraper import PropertyInfo


@csrf_exempt
def property_info(request):
    if request.method == 'POST':
        input_string = request.POST.get('listing_url')

        house = PropertyInfo(input_string)
        property_info_resp = house.get_property_info()
        return JsonResponse({'data': property_info_resp})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
