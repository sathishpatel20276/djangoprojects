from django.shortcuts import render
from fakeapp.models import FakeData
from django.http.response import HttpResponse
import faker
fake = faker.Faker()

def fake_view(request):
    for i in range(2000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        job = fake.random_element(elements=('HR', 'TL', 'PM', 'Admin'))
        company = fake.random_element(
            elements=('Micropyramid', 'DjangoGirls', 
            'TCS', 'Infosys', 'Deloitte'))
        salary = fake.random_element(
            elements=(10000, 15000, 20000, 25000, 30000))
        city = fake.random_element(
            elements=('Bbsr', 'Hyd', 'Bang', 'puna', 'patna'))
        dob = fake.date_time()
        address = fake.address()

        data = FakeData(
            first_name=first_name,
            last_name=last_name,
            email=email,
            job=job,
            company=company,
            salary=salary,
            city=city,
            dob=dob,
            address=address)
        data.save()
    return HttpResponse('Ojacers Data Inserted')

