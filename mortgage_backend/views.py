from django.shortcuts import render
from django.contrib import admin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from finny_scraper import PropertyInfo
from .models import County, LoanLimit
from django.core import serializers
from django.shortcuts import get_object_or_404
import urllib.parse


@csrf_exempt
def property_info(request):

    input_string = request.GET.get('listing_url')
    house = PropertyInfo(input_string)
    property_info_resp = house.get_property_info()
    return JsonResponse({'data': property_info_resp})


def loan_limit_by_county(request):
    county_name = request.GET.get('county_name')
    state_abbr = request.GET.get('state_abbr')
    decoded_county_name = urllib.parse.unquote_plus(county_name).upper()

    try:
        county = County.objects.get(county_name__iexact=decoded_county_name,
                                    state_abbr__iexact=state_abbr)
        loan_limit = LoanLimit.objects.get(county=county)
        response_data = {
            'county_name': county.county_name,
            'fha': {
                'one_unit': loan_limit.fha_one_unit,
                'two_unit': loan_limit.fha_two_unit,
                'three_unit': loan_limit.fha_three_unit,
                'four_unit': loan_limit.fha_four_unit,
                'effective_date': loan_limit.fha_effective_date.isoformat(),
            },
            'conventional': {
                'one_unit': loan_limit.conventional_one_unit,
                'two_unit': loan_limit.conventional_two_unit,
                'three_unit': loan_limit.conventional_three_unit,
                'four_unit': loan_limit.conventional_four_unit,
                'effective_date': loan_limit.conventional_effective_date.isoformat(),
            }
        }
        return JsonResponse({'data': response_data})
    except County.DoesNotExist:
        return JsonResponse({'error': 'County not found'})


def county_list(request):
    state_abbr = request.GET.get('state_abbr')
    if state_abbr is None:
        counties = County.objects.all()
    else:
        counties = County.objects.filter(state_abbr__iexact=state_abbr)

    return JsonResponse({'data': list(counties.values('id', 'county_name', 'state_abbr'))})
