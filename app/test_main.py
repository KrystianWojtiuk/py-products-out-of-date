from typing import Generator

from app.main import outdated_products
import datetime
from unittest.mock import patch
import pytest


@pytest.mark.parametrize(
    "product_list, today_date, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600},
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120},
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            datetime.date(2022, 2, 2),
            ["duck"],
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600},
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120},
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            datetime.date(2023, 2, 2),
            ["salmon", "chicken", "duck"],
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600},
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120},
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            datetime.date(2021, 2, 2),
            [],
        ),
    ]
)
@patch("app.main.datetime.date")
def test_outdated_products(
        mock_date: Generator,
        product_list: list,
        today_date: datetime.date,
        expected: list
) -> None:
    mock_date.today.return_value = today_date
    assert outdated_products(product_list) == expected
