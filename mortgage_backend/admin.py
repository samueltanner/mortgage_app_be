from django.contrib import admin
from .models import County, LoanLimitOption

# Register your models here.

admin.site.register(County)
admin.site.register(LoanLimitOption)
