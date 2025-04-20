from unittest.mock import patch
import pytest
import datetime
from app.main import outdated_products
from typing import Generator


@pytest.fixture
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.fixture()
def mocked_date() -> Generator:
    with patch("app.main.datetime.date.today") as mock_date:
        yield mock_date


def test_date_earlier_than_all(
        products: list,
        mocked_date: Generator
) -> None:
    mocked_date.return_value = datetime.date(2022, 1, 1)
    assert outdated_products(products) == [
        "salmon",
        "chicken",
        "duck",
    ]


def test_date_later_than_all(
        products: list,
        mocked_date: Generator
) -> None:
    mocked_date.return_value = datetime.date(2023, 3, 1)
    assert outdated_products(products) == []


def test_date_equals_middle(
        products: list,
        mocked_date: Generator
) -> None:
    mocked_date.return_value = datetime.date(2022, 2, 5)
    assert outdated_products(products) == ["salmon"]
