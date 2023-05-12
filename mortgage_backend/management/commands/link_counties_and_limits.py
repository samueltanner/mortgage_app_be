from django.core.management.base import BaseCommand
from mortgage_backend.models import County, LoanLimitOption, LoanLimit


class Command(BaseCommand):
    help = 'Populates County objects with LoanLimitOption objects based on LoanLimit model data'

    def handle(self, *args, **options):
        counties = County.objects.all()
        for county in counties:
            loan_limit = county.loanlimit_set.first()
            fha_one_unit_limit = loan_limit.fha_one_unit
            fha_two_unit_limit = loan_limit.fha_two_unit
            fha_three_unit_limit = loan_limit.fha_three_unit
            fha_four_unit_limit = loan_limit.fha_four_unit
            conventional_one_unit_limit = loan_limit.conventional_one_unit
            conventional_two_unit_limit = loan_limit.conventional_two_unit
            conventional_three_unit_limit = loan_limit.conventional_three_unit
            conventional_four_unit_limit = loan_limit.conventional_four_unit

            loan_options = LoanLimitOption.objects.all()
            fha_loan_option = loan_options.filter(one_unit=fha_one_unit_limit, two_unit=fha_two_unit_limit,
                                                  three_unit=fha_three_unit_limit, four_unit=fha_four_unit_limit)
            conventional_loan_option = loan_options.filter(one_unit=conventional_one_unit_limit, two_unit=conventional_two_unit_limit,
                                                           three_unit=conventional_three_unit_limit, four_unit=conventional_four_unit_limit)

            county.fha_loan_limits.add(*fha_loan_option)
            county.conventional_loan_limits.add(*conventional_loan_option)
            county.save()
        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
