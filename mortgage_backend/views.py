from django.shortcuts import render
from django.contrib import admin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from finny_scraper import PropertyInfo
from .models import County
import urllib.parse
from finny_scraper_local.utils import PropertyInfo


@csrf_exempt
def property_info(request):

    listing_url = request.GET.get('listing_url')
    loan_limits_boolean = request.GET.get('get_loan_limits')
    house = PropertyInfo(listing_url)
    property_info_resp = house.get_property_info()
    if loan_limits_boolean == 'true':
        address = property_info_resp['address']
        county_name = address['county'].upper()
        state_abbr = address['state']
        loan_limits = loan_limit_by_county(
            county_name=county_name, state_abbr=state_abbr)
        property_info_resp['loan_limits'] = loan_limits
    return(JsonResponse(property_info_resp))


def loan_limit_by_county(request=None, county_name=None, state_abbr=None):
    if request:
        county_name = request.GET.get('county_name')
        state_abbr = request.GET.get('state_abbr')
    decoded_county_name = urllib.parse.unquote_plus(county_name).upper()

    try:
        county = County.objects.get(county_name__iexact=decoded_county_name,
                                    state_abbr__iexact=state_abbr)
        fha_loan_limit = county.fha_loan_limits.first()
        conventional_loan_limit = county.conventional_loan_limits.first()
        response_data = {
            'county_name': county.county_name,
            'fha': {
                'one_unit': fha_loan_limit.one_unit,
                'two_unit': fha_loan_limit.two_unit,
                'three_unit': fha_loan_limit.three_unit,
                'four_unit': fha_loan_limit.four_unit,
                'effective_date': fha_loan_limit.effective_date.isoformat(),
            },
            'conventional': {
                'one_unit': conventional_loan_limit.one_unit,
                'two_unit': conventional_loan_limit.two_unit,
                'three_unit': conventional_loan_limit.three_unit,
                'four_unit': conventional_loan_limit.four_unit,
                'effective_date': conventional_loan_limit.effective_date.isoformat(),
            }
        }
        if request:
            return JsonResponse(response_data)
        else:
            return response_data
    except County.DoesNotExist:
        if request:
            return JsonResponse({'error': 'County not found'})
        else:
            return {'error': 'County not found'}


def county_list(request):
    state_abbr = request.GET.get('state_abbr')
    if state_abbr is None or state_abbr == '':
        counties = County.objects.all()
    else:
        counties = County.objects.filter(state_abbr__iexact=state_abbr)

    return JsonResponse({'data': list(counties.values('id', 'county_name', 'state_abbr'))})
