from django.contrib import admin
from .models import County, LoanLimit, LoanLimitOption

# Register your models here.

admin.site.register(County)
admin.site.register(LoanLimit)
admin.site.register(LoanLimitOption)
