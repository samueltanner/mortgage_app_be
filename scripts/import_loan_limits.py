# import csv
# from mortgage_backend.models import County, ConventionalLoanLimit, FHALoanLimit

# conventional_dict = {}
# fha_dict = {}

# with open('mortgage_backend/loan_limits.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     next(reader)
#     for row in reader:
#         state_abbr = row[1]
#         county_name = row[4]
#         county = County.objects.get(
#             state_abbr=state_abbr, county_name=county_name)

#         conventional_key = (row[7], row[8], row[9], row[10])
#         if conventional_key in conventional_dict:
#             cl = conventional_dict[conventional_key]
#         else:
#             cl = ConventionalLoanLimit.objects.create(
#                 one_unit=row[7],
#                 two_unit=row[8],
#                 three_unit=row[9],
#                 four_unit=row[10],
#                 effective_date='2023-01-01'
#             )
#             conventional_dict[conventional_key] = cl

#         fha_key = (row[13], row[14], row[15], row[16])
#         if fha_key in fha_dict:
#             fh = fha_dict[fha_key]
#         else:
#             fh = FHALoanLimit.objects.create(
#                 one_unit=row[13],
#                 two_unit=row[14],
#                 three_unit=row[15],
#                 four_unit=row[16],
#                 effective_date='2023-01-01'
#             )
#             fha_dict[fha_key] = fh

#         cl.counties.add(county)
#         fh.counties.add(county)
