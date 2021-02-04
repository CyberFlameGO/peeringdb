import pytest
import json
import re
import os

from django.test import Client, TestCase, RequestFactory
from django.contrib.auth.models import Group, AnonymousUser
from django.contrib.auth import get_user
from django.core.management import call_command
from django.core.exceptions import ValidationError

import peeringdb_server.models as models


@pytest.fixture
def fac():
    fac = models.Facility(
        name="Geocode Fac",
        status="ok",
        address1="Some street",
        address2="",
        city="Chicago",
        country="US",
        state="IL",
        zipcode="1234",
    )
    return fac


def load_json(filename):
    with open(
        os.path.join(
            os.path.dirname(__file__),
            "data",
            "geo",
            f"{filename}.json",
        ),
    ) as fh:
        json_data = json.load(fh)
    return json_data


@pytest.fixture
def reverse():
    return load_json("reverse")


@pytest.fixture
def reverse_parsed():
    return load_json("reverse_parsed")


def test_geo_model_defaults(fac):
    assert fac.geocode_status == False
    assert fac.geocode_date == None


def test_geo_model_geocode_coordinates(fac):
    assert fac.geocode_coordinates == None
    fac.latitude = 41.876212
    fac.longitude = -87.631453
    assert fac.geocode_coordinates == (41.876212, -87.631453)


def test_geo_model_geocode_addresss(fac):
    assert fac.geocode_address == "Some street , Chicago, IL 1234"


def test_geo_model_get_address1(fac):
    data = [{"empty": "empty"}]
    assert fac.get_address1_from_geocode(data) == None

    data = load_json("address1_test0")
    assert fac.get_address1_from_geocode(data) == "427 S LaSalle St"

    data = load_json("address1_test1")
    assert fac.get_address1_from_geocode(data) == "427"

    data = load_json("address1_test2")
    assert fac.get_address1_from_geocode(data) == "S LaSalle St"


def test_geo_model_reverse_geocode_blank(fac):
    with pytest.raises(ValidationError) as exc:
        fac.reverse_geocode(None)
    message = "Latitude and longitude must be defined for reverse geocode lookup"
    assert message in str(exc.value)


def test_geo_model_parse_reverse(fac, reverse, reverse_parsed):
    assert fac.parse_reverse_geocode(reverse) == reverse_parsed
