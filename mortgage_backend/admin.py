from django.contrib import admin
from .models import County, LoanLimit

# Register your models here.

admin.site.register(County)
admin.site.register(LoanLimit)
