import os.path

import pytest

from main import app, PATH
from utils import *


def test_load_json():
    json_data = load_json(os.path.join('..', PATH))
    assert type(json_data) == list, f'Ошибка загрузки данных из "{PATH}"!'
    for d in json_data:
        assert type(d) == dict, f'Ошибка! Внутри JSON-файла "{PATH}" нет словарей!'


def test_load_json_if_not_found():
    with pytest.raises(FileNotFoundError):
        assert load_json('file_not_found.json')


def test_key_date(operation_dict):
    date = key_date(operation_dict)
    assert date.strftime('%d.%m.%Y') == '11.01.2022'


@pytest.mark.parametrize('type_, expected_1, expected_2',
                         [
                             ('from', 'Visa Platinum', '1111 22** **** 4444'),
                             ('to', 'Счет', '**7890')
                         ]
                         )
def test_get_data_from_operation(operation_dict, type_, expected_1, expected_2):
    one, two = get_data_from_operation(operation_dict, type_)

    assert one == expected_1
    assert two == expected_2