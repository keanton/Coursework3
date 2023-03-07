import pytest


@pytest.fixture
def operation_dict():
    return {
        "id": 123456789,
        "state": "EXECUTED",
        "date": "2022-01-11T10:00:00.000000",
        "operationAmount": {
            "amount": "777.77",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1111222233334444",
        "to": "Счет 12345678901234567890"
    }