import json
from datetime import datetime


def load_json(path: str) -> list[dict] | str:
    """
    Loads data from JSON

    :param path:
        path to JSON-file with operations
    :return:
        list of dicts (one dict - one operation)
        """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def key_date(operation: dict) -> datetime.date:
    """
    Gets a date in string format from an operation and return a datetime object

    :param operation:
        dict with operation data
    :return:
        datetime.date object with date of operation
        if no key 'date' in dict return date '0001-01-01'
    """
    if 'date' in operation:
        datetime_str = operation['date'].split('T')[0]
        return datetime.strptime(datetime_str, '%Y-%m-%d')
    return datetime.fromisoformat('0001-01-01')


def get_data_from_operation(operation: dict, type_: str) -> tuple[str, str]:
    """
    Processes the operation data and returns the account/card name and account/card number

    :param operation:
        dict with operation data
    :param type_:
        type of operation ('from' or 'to')
    :return:
        Returns the name and number of the account or card
    """
    if type_ in operation:
        acc_or_card_name = ' '.join(operation[type_].split()[:-1])
        acc_card = operation[type_].split(' ')[-1]
        number = ''
        if 'Счет' in acc_or_card_name:
            number = '**' + acc_card[-4:]
        else:
            for i in range(len(acc_card)):
                if 6 <= i < 12:
                    number += '*'
                else:
                    number += acc_card[i]
                if (i + 1) % 4 == 0 and i != 15:
                    number += ' '
    elif 'Открытие' in operation['description']:
        return 'Пополнение', ''
    else:
        acc_or_card_name, number = '', ''
    return acc_or_card_name, number