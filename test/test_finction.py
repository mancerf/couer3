from until.function import get_formatted_data, get_filtered_data, get_last_values
from test.conftest import test_datas

test_data = test_datas()
def test_get_filtered_data():
    assert get_filtered_data(test_data[:2]) ==[
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }
    ]
def test_get_last_values():
    data = get_last_values(test_data, 3)
    assert [x["date"] for x in data] == ["2018-11-29T07:18:23.941293", "2018-10-14T08:21:33.419441", "2018-09-12T21:27:25.241689"]


def test_get_formatted_data():
    data = get_formatted_data(test_data)
    assert data == ['        19.08.2018 Перевод с карты на карту\n        Visa Classic 683 98** **** 7658 -> Visa Platinum 899 92** **** 5229\n        56883.54 USD', '        12.09.2018 Перевод организации\n        Visa Platinum 124 37** **** 3588 -> Счет **1657\n        67314.70 руб.', '        14.10.2018 Перевод с карты на счет\n        Maestro 392 54** **** 4026 -> Счет **3493\n        77751.04 руб.', '        26.01.2018 Перевод с карты на счет\n        Maestro 459 30** **** 4501 -> Счет **5086\n        50870.71 руб.', '        29.11.2018 Перевод с карты на карту\n        MasterCard 315 47** **** 5065 -> Visa Gold 944 34** **** 5960\n        3348.98 USD', '        14.04.2018 Перевод организации\n        Счет **8655 -> Счет **8967\n        96995.73 руб.']