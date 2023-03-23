from django.contrib import admin
from django.urls import path
from mortgage_backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('property_info/', views.property_info, name='listing_url'),

]
