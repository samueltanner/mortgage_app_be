from django.db import models

# Create your models here.


class County(models.Model):
    county_name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    state_abbr = models.CharField(max_length=10)
    median_home_value = models.IntegerField()
    fha_loan_limits = models.ManyToManyField(
        'LoanLimitOption', related_name='fha_loan_limits')
    conventional_loan_limits = models.ManyToManyField(
        'LoanLimitOption', related_name='conventional_loan_limits')

    def __str__(self):
        return self.county_name

class LoanLimitOption(models.Model):
    one_unit = models.IntegerField()
    two_unit = models.IntegerField()
    three_unit = models.IntegerField()
    four_unit = models.IntegerField()
    effective_date = models.DateField(default='2023-01-01')

    def __str__(self):
        return self.get_unit_string()

    def get_unit_string(self):
        return f"{self.effective_date} | {self.one_unit}...{self.four_unit}"
