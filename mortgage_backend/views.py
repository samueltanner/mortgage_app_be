from django.shortcuts import render
from django.contrib import admin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from finny_scraper import PropertyInfo


@csrf_exempt
def process_string(request):
    if request.method == 'POST':
        input_string = request.POST.get('process_string')
        print(request.POST.get('process_string'))

        house = PropertyInfo(input_string)
        property_info = house.get_property_info()
        # process input_string using your package
        # result = myfunction(input_string)
        return JsonResponse({'data': property_info})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
# Create your views here.
