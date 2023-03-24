from django.db import models

# Create your models here.


class County(models.Model):
    county_name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    state_abbr = models.CharField(max_length=10)
    median_home_value = models.IntegerField()

    def __str__(self):
        return self.county_name


class LoanLimit(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    conventional_one_unit = models.IntegerField()
    conventional_two_unit = models.IntegerField()
    conventional_three_unit = models.IntegerField()
    conventional_four_unit = models.IntegerField()
    fha_one_unit = models.IntegerField()
    fha_two_unit = models.IntegerField()
    fha_three_unit = models.IntegerField()
    fha_four_unit = models.IntegerField()
    conventional_effective_date = models.DateField(default='2023-01-01')
    fha_effective_date = models.DateField(default='2023-01-01')

    def __str__(self):
        return self.county.county_name


class LoanLimitOption(models.Model):
    one_unit = models.IntegerField()
    two_unit = models.IntegerField()
    three_unit = models.IntegerField()
    four_unit = models.IntegerField()
    effective_date = models.DateField(default='2023-01-01')

    def __str__(self):
        return self.get_unit_string()

    def get_unit_string(self):
        return f"{self.one_unit}-{self.two_unit}-{self.three_unit}-{self.four_unit}"
