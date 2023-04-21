from django.contrib import admin
from django.urls import path
from mortgage_backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('property_info/', views.property_info, name='listing_info'),
    path('loan_limit_by_county/', views.loan_limit_by_county, name='loan_limits'),
    path('county_list/', views.county_list, name='county_list'),
    path('interest_rates/', views.interest_rates, name='interest_rates')
]
