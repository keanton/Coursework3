from datetime import datetime

from utils import load_json, key_date, get_data_from_operation

PATH = 'operations.json'


def app():
    data.sort(key=key_date, reverse=True)  # sorts the list by dates from the latest date

    printed = 0
    index = 0

    while printed < 5:
        operation = data[index]

        if operation['state'] == 'EXECUTED':
            date = datetime.strptime(operation["date"].split("T")[0], '%Y-%m-%d')
            date = date.strftime('%d.%m.%Y')

            from_, acc1 = get_data_from_operation(operation, "from")
            to_, acc2 = get_data_from_operation(operation, "to")

            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']

            print(f'{date} {operation["description"]}\n'
                  f'{from_} {acc1} -> {to_} {acc2}\n'
                  f'{amount} {currency}\n')

            printed += 1
        index += 1


if __name__ == '__main__':
    data = load_json(PATH)

    if type(data) == str:
        print(f'Ошибка: {data}')
    else:
        app()