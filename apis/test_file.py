from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

# Create your tests here.
from .models import country ,city
import pytest

pytestmark = pytest.mark.django_db


@pytest.fixture()
def setup() -> city:
    cou = country.objects.create(country = "newzland")
    cit = city.objects.create(city = "new" , level="2nd" ,country=cou)
    return cit


def test_1(setup):
    client = APIClient()
    url = reverse("home")
    res = client.get(url)
    response = client.post(path=url, data={"id": 1, "country": "usa"})

    assert res.status_code == 200
    assert response.status_code == 201

def test_2(setup):
    setup  = setup
    client = APIClient()
    url = reverse("edit" , kwargs={'pk': '1'} )
    res = client.get(url)
    response = client.put(path=url, data={
        "country": "germany"
         })

    assert res.status_code == 200
    assert response.status_code == 202



