
from datetime import datetime


def get_filtered_data(datas):
    new_data = [x for x in datas if "state" in x and x["state"] == "EXECUTED"]
    return new_data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:count_last_values]
    return data


def hide_bill(date):
    date_list = date.split(' ')
    name_card = date_list[0:-1]
    if len(name_card) == 2:
        name_card = str(name_card[0]) + ' ' + str(name_card[1])
    else:
        name_card = str(name_card[0])
    number_card = str((date_list[-1:])[0])
    if len(number_card) == 16:
        bill = f"{name_card} {number_card[0:3]} {number_card[4:6]}** **** {number_card[-4:]}"
    else:
        bill = f"{name_card} **{number_card[-4:]}"

    return bill


def get_formatted_data(datas):
    formatted_data = []
    for data in datas:
        data["date"] = datetime.strptime(data["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")

        if "from" in data:
            formatted_data.append(f"""\
        {data['date']} {data["description"]}
        {hide_bill(data["from"])} -> {hide_bill(data["to"])}
        {data["operationAmount"]["amount"]} {data["operationAmount"]["currency"]["name"]}""")
        else:
            formatted_data.append(f"""\
        {data['date']} {data["description"]}
        {hide_bill(data["to"])}
        {data["operationAmount"]["amount"]} {data["operationAmount"]["currency"]["name"]}""")

    return formatted_data
