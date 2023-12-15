# Generate fake addresses for the UK
# 2023 Karol Chlasta - Data Science Summit 2023

from faker import Faker
import csv

FakeData = Faker(['en_UK'])

def generate_ukaddr():
    return [FakeData.building_number(), FakeData.street_name(), FakeData.city_suffix(), FakeData.postcode(), FakeData.city(),'invalid']

with open('invalid_ukaddr.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerow(['Building', 'Street', 'Locality', 'Postcode', 'Posttown', 'Validity'])
    for n in range(1, 575128):
        writer.writerow(generate_ukaddr())